// ═══════════════════════════════════════════
//  ADEXPERT — Rate Limiter & Request Logger
//  Inclure dans index.html avec :
//  <script src="rate_limiter.js"></script>
//  (avant le script principal)
// ═══════════════════════════════════════════

var RateLimiter = (function () {

  // ─── Configuration ───────────────────────
  var CONFIG = {
    max_par_minute:   30,   // max requêtes par minute par user
    max_par_heure:   200,   // max requêtes par heure par user
    max_par_jour:   1000,   // max requêtes par jour par user
    log_max_entrees: 500,   // nb max d'entrées gardées en log
  };

  // ─── Clés localStorage ───────────────────
  var KEY_LOG     = 'adexpert_req_log';
  var KEY_BLOCKED = 'adexpert_blocked_until';

  // ─── Helpers ─────────────────────────────
  function now() { return Date.now(); }
  function getLog() {
    try { return JSON.parse(localStorage.getItem(KEY_LOG) || '[]'); }
    catch (e) { return []; }
  }
  function saveLog(log) {
    // Garder seulement les CONFIG.log_max_entrees dernières entrées
    if (log.length > CONFIG.log_max_entrees) {
      log = log.slice(log.length - CONFIG.log_max_entrees);
    }
    try { localStorage.setItem(KEY_LOG, JSON.stringify(log)); }
    catch (e) { /* localStorage plein — on vide */ localStorage.removeItem(KEY_LOG); }
  }

  // ─── Vérifier si l'user est bloqué ───────
  function estBloque() {
    var until = parseInt(localStorage.getItem(KEY_BLOCKED) || '0');
    if (until > now()) return true;
    if (until) localStorage.removeItem(KEY_BLOCKED);
    return false;
  }

  function bloquerPour(ms, raison) {
    var until = now() + ms;
    localStorage.setItem(KEY_BLOCKED, String(until));
    console.warn('[RateLimiter] Bloqué jusqu\'à ' +
      new Date(until).toLocaleTimeString('fr-FR') + ' — ' + raison);
  }

  // ─── Compter les requêtes sur une fenêtre ─
  function compterDepuis(log, depuisMs) {
    var seuil = now() - depuisMs;
    return log.filter(function (e) { return e.ts >= seuil; }).length;
  }

  // ─── Enregistrer une requête ──────────────
  function enregistrer(url, method) {
    var log = getLog();
    log.push({
      ts:       now(),
      url:      url,
      method:   (method || 'GET').toUpperCase(),
      user:     (localStorage.getItem('username') || 'inconnu'),
      date:     new Date().toISOString(),
    });
    saveLog(log);
  }

  // ─── Vérifier les limites ─────────────────
  function verifierLimites() {
    var log = getLog();
    var parMin    = compterDepuis(log, 60 * 1000);
    var parHeure  = compterDepuis(log, 60 * 60 * 1000);
    var parJour   = compterDepuis(log, 24 * 60 * 60 * 1000);

    if (parMin >= CONFIG.max_par_minute) {
      bloquerPour(30 * 1000, parMin + ' req/min — pause 30s');
      return false;
    }
    if (parHeure >= CONFIG.max_par_heure) {
      bloquerPour(5 * 60 * 1000, parHeure + ' req/h — pause 5min');
      return false;
    }
    if (parJour >= CONFIG.max_par_jour) {
      bloquerPour(60 * 60 * 1000, parJour + ' req/jour — pause 1h');
      return false;
    }
    return true;
  }

  // ─── API publique ─────────────────────────

  /**
   * Appeler AVANT chaque fetch().
   * Retourne true si la requête est autorisée, false si bloquée.
   */
  function autoriser(url, method) {
    if (estBloque()) {
      var until = parseInt(localStorage.getItem(KEY_BLOCKED) || '0');
      var restant = Math.ceil((until - now()) / 1000);
      console.warn('[RateLimiter] Requête bloquée — encore ' + restant + 's d\'attente');
      return false;
    }
    if (!verifierLimites()) return false;
    enregistrer(url, method);
    return true;
  }

  /**
   * Retourne les stats du jour pour affichage.
   */
  function stats() {
    var log = getLog();
    return {
      par_minute: compterDepuis(log, 60 * 1000),
      par_heure:  compterDepuis(log, 60 * 60 * 1000),
      par_jour:   compterDepuis(log, 24 * 60 * 60 * 1000),
      limites:    CONFIG,
      bloque:     estBloque(),
    };
  }

  /**
   * Retourne le log brut (pour export/debug).
   */
  function exportLog() {
    return getLog();
  }

  /**
   * Télécharge le log du jour en CSV.
   */
  function telechargerLog() {
    var log = getLog();
    var aujourdhui = new Date().toISOString().slice(0, 10);
    var filtre = log.filter(function (e) {
      return e.date && e.date.slice(0, 10) === aujourdhui;
    });

    var csv = 'Date,Heure,Utilisateur,Methode,URL\n';
    filtre.forEach(function (e) {
      var d = new Date(e.ts);
      csv += [
        d.toLocaleDateString('fr-FR'),
        d.toLocaleTimeString('fr-FR'),
        e.user,
        e.method,
        '"' + (e.url || '') + '"'
      ].join(',') + '\n';
    });

    var blob = new Blob([csv], { type: 'text/csv;charset=utf-8' });
    var url  = URL.createObjectURL(blob);
    var a    = document.createElement('a');
    a.href     = url;
    a.download = 'adexpert_log_' + aujourdhui + '.csv';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 5000);
  }

  /**
   * Vide le log (admin seulement).
   */
  function viderLog() {
    localStorage.removeItem(KEY_LOG);
    localStorage.removeItem(KEY_BLOCKED);
    console.info('[RateLimiter] Log vidé.');
  }

  return {
    autoriser:      autoriser,
    stats:          stats,
    exportLog:      exportLog,
    telechargerLog: telechargerLog,
    viderLog:       viderLog,
    config:         CONFIG,
  };

})();


// ═══════════════════════════════════════════
//  INTÉGRATION AUTOMATIQUE dans la fonction api()
//  Remplace ta fonction api() existante par celle-ci
// ═══════════════════════════════════════════

/*

async function api(url, opts) {

  // ── Rate limiting ──────────────────────
  if (!RateLimiter.autoriser(url, (opts && opts.method) || 'GET')) {
    var s = RateLimiter.stats();
    var restant = s.bloque
      ? 'Trop de requêtes — veuillez patienter.'
      : 'Limite atteinte.';
    throw new Error(restant);
  }
  // ── Reste identique à ton api() actuel ──

  opts = opts || {};
  var h = Object.assign(
    { 'Content-Type': 'application/json' },
    S.token ? { 'Authorization': 'Token ' + S.token } : {},
    opts.headers || {}
  );
  var r = await fetch(BASE + url, Object.assign({}, opts, { headers: h }));
  if (r.status === 401) { doLogout(); return null; }
  if (r.status === 403) { showAlert(null, 'Accès refusé.', true); return null; }
  if (!r.ok) {
    var eBody = await r.json().catch(() => ({}));
    var msg = '';
    if (typeof eBody === 'object' && eBody !== null) {
      msg = Object.entries(eBody).map(([k, v]) => {
        var vals = Array.isArray(v) ? v.join(', ') : String(v);
        return k === 'non_field_errors' || k === 'detail' ? vals : k + ': ' + vals;
      }).join(' | ');
    }
    throw new Error(msg || JSON.stringify(eBody));
  }
  if (r.status === 204) return null;
  return r.json();
}

*/


// ═══════════════════════════════════════════
//  COMMANDES UTILES (console du navigateur)
// ═══════════════════════════════════════════
//
//  Voir les stats en temps réel :
//    RateLimiter.stats()
//
//  Télécharger le log du jour en CSV :
//    RateLimiter.telechargerLog()
//
//  Voir le log brut :
//    RateLimiter.exportLog()
//
//  Vider le log (admin) :
//    RateLimiter.viderLog()
//
// ═══════════════════════════════════════════