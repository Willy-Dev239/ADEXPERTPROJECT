/* ═══════════════════════════════════════════════════════════════
   ADEXPERT — MODULE i18n (Traduction 8 langues)
   FR, EN, RN (Kirundi), SW (Swahili), RW (Kinyarwanda), IT, ES, ZH
   ⚠️ Les traductions RN / RW ont été générées automatiquement.
      Faites-les relire par un locuteur natif avant mise en prod.
   ═══════════════════════════════════════════════════════════════ */

const I18N_LANGS = {
  fr: '🇫🇷 Français',
  en: '🇬🇧 English',
  rn: '🇧🇮 Kirundi',
  sw: '🇹🇿 Kiswahili',
  rw: '🇷🇼 Kinyarwanda',
  it: '🇮🇹 Italiano',
  es: '🇪🇸 Español',
  zh: '🇨🇳 中文'
};

const I18N = {
  // ── NAVIGATION SIDEBAR ─────────────────────────────────────────
  'nav.principal': {fr:'Principal',en:'Main',rn:'Ibanze',sw:'Kuu',rw:'Ibanze',it:'Principale',es:'Principal',zh:'主要'},
  'nav.dashboard': {fr:'Tableau de bord',en:'Dashboard',rn:'Ikibaho',sw:'Dashibodi',rw:'Ikibaho',it:'Pannello',es:'Panel',zh:'仪表盘'},
  'nav.gestion': {fr:'Gestion',en:'Management',rn:'Ubuyobozi',sw:'Usimamizi',rw:'Ubuyobozi',it:'Gestione',es:'Gestión',zh:'管理'},
  'nav.proprietaires': {fr:'Propriétaires',en:'Owners',rn:'Abanyene',sw:'Wamiliki',rw:'Abanyirai',it:'Proprietari',es:'Propietarios',zh:'业主'},
  'nav.immeubles': {fr:'Immeubles',en:'Buildings',rn:'Amazu',sw:'Majengo',rw:'Inyubako',it:'Edifici',es:'Edificios',zh:'楼宇'},
  'nav.locaux': {fr:'Locaux',en:'Units',rn:'Ivyumba',sw:'Vyumba',rw:'Ibyumba',it:'Locali',es:'Locales',zh:'房间'},
  'nav.locataires': {fr:'Locataires',en:'Tenants',rn:'Abakode',sw:'Wapangaji',rw:'Abakode',it:'Inquilini',es:'Inquilinos',zh:'租户'},
  'nav.contrats': {fr:'Contrats Location',en:'Lease Contracts',rn:'Amasezerano yo Gukodesha',sw:'Mikataba ya Kukodisha',rw:'Amasezerano yo Gukodesha',it:'Contratti di Locazione',es:'Contratos de Alquiler',zh:'租赁合同'},
  'nav.contrats_societe': {fr:'Contrats Société',en:'Company Contracts',rn:'Amasezerano y\'Isosiyete',sw:'Mikataba ya Kampuni',rw:'Amasezerano y\'Isosiyete',it:'Contratti Società',es:'Contratos de la Empresa',zh:'公司合同'},
  'nav.loyers': {fr:'Loyers & Paiements',en:'Rents & Payments',rn:'Amakodo n\'Ivyishuwe',sw:'Kodi na Malipo',rw:'Ubukode n\'Ubwishyu',it:'Affitti e Pagamenti',es:'Alquileres y Pagos',zh:'租金与付款'},
  'nav.bordereaux': {fr:'Bordereaux',en:'Payment Slips',rn:'Impapuro z\'Ivyishuwe',sw:'Risiti za Malipo',rw:'Impapuro z\'Ubwishyu',it:'Distinte',es:'Comprobantes',zh:'凭单'},
  'nav.virements': {fr:'Virements Propriétaires',en:'Owner Transfers',rn:'Ivyishuwe ku Banyene',sw:'Uhamisho wa Wamiliki',rw:'Ubwishyu ku Banyirai',it:'Bonifici Proprietari',es:'Transferencias a Propietarios',zh:'业主转账'},
  'nav.analyse': {fr:'Analyse',en:'Analytics',rn:'Isesengura',sw:'Uchambuzi',rw:'Isesengura',it:'Analisi',es:'Análisis',zh:'分析'},
  'nav.rapports': {fr:'Rapports',en:'Reports',rn:'Raporo',sw:'Ripoti',rw:'Raporo',it:'Report',es:'Informes',zh:'报告'},
  'nav.portefeuille': {fr:'Portefeuille',en:'Portfolio',rn:'Igikoresho c\'Amahera',sw:'Kwingi wa Fedha',rw:'Icyegeranyo',it:'Portafoglio',es:'Cartera',zh:'投资组合'},
  'nav.communication': {fr:'Communication',en:'Communication',rn:'Itumanaho',sw:'Mawasiliano',rw:'Itumanaho',it:'Comunicazione',es:'Comunicación',zh:'沟通'},
  'nav.chat': {fr:'Chat Immeubles',en:'Buildings Chat',rn:'Ikiganiro c\'Amazu',sw:'Mazungumzo ya Majengo',rw:'Ikiganiro cy\'Inyubako',it:'Chat Edifici',es:'Chat de Edificios',zh:'楼宇聊天'},
  'nav.notifications': {fr:'Notifications',en:'Notifications',rn:'Amamenyesha',sw:'Arifa',rw:'Amamenyesha',it:'Notifiche',es:'Notificaciones',zh:'通知'},
  'nav.utilisateurs': {fr:'Gestion des Utilisateurs',en:'User Management',rn:'Ubuyobozi bw\'Abakoresha',sw:'Usimamizi wa Watumiaji',rw:'Ubuyobozi bw\'Abakoresha',it:'Gestione Utenti',es:'Gestión de Usuarios',zh:'用户管理'},
  'nav.administration': {fr:'Administration',en:'Administration',rn:'Ubuyobozi',sw:'Utawala',rw:'Ubuyobozi',it:'Amministrazione',es:'Administración',zh:'管理员'},

  // ── TOPBAR ─────────────────────────────────────────────────────
  'topbar.add': {fr:'+ Ajouter',en:'+ Add',rn:'+ Ongeraho',sw:'+ Ongeza',rw:'+ Ongeraho',it:'+ Aggiungi',es:'+ Añadir',zh:'+ 添加'},
  'topbar.logout': {fr:'Déconnexion',en:'Logout',rn:'Gusohoka',sw:'Toka',rw:'Gusohoka',it:'Disconnetti',es:'Cerrar sesión',zh:'退出登录'},
  'topbar.language': {fr:'Langue',en:'Language',rn:'Ururimi',sw:'Lugha',rw:'Ururimi',it:'Lingua',es:'Idioma',zh:'语言'},

  // ── RÔLES ──────────────────────────────────────────────────────
  'role.admin': {fr:'Administrateur',en:'Administrator',rn:'Umuyobozi',sw:'Msimamizi',rw:'Umuyobozi',it:'Amministratore',es:'Administrador',zh:'管理员'},
  'role.gestionnaire': {fr:'Gestionnaire',en:'Manager',rn:'Umuyobozi w\'agateka',sw:'Meneja',rw:'Umuyobozi',it:'Gestore',es:'Gestor',zh:'经理'},
  'role.lecteur': {fr:'Lecteur',en:'Viewer',rn:'Umusomyi',sw:'Msomaji',rw:'Umusomyi',it:'Lettore',es:'Lector',zh:'查看者'},

  // ── DASHBOARD ──────────────────────────────────────────────────
  'dash.filtrer_par': {fr:'Filtrer par',en:'Filter by',rn:'Guca',sw:'Chuja kwa',rw:'Shungura',it:'Filtra per',es:'Filtrar por',zh:'筛选'},
  'dash.tous_proprietaires': {fr:'Tous les propriétaires',en:'All owners',rn:'Abanyene bose',sw:'Wamiliki wote',rw:'Abanyirai bose',it:'Tutti i proprietari',es:'Todos los propietarios',zh:'所有业主'},
  'dash.tous_immeubles': {fr:'Tous les immeubles',en:'All buildings',rn:'Amazu yose',sw:'Majengo yote',rw:'Inyubako zose',it:'Tutti gli edifici',es:'Todos los edificios',zh:'所有楼宇'},
  'dash.reinitialiser': {fr:'Réinitialiser',en:'Reset',rn:'Gusubira ku ntango',sw:'Weka upya',rw:'Ongera utangire',it:'Reimposta',es:'Restablecer',zh:'重置'},
  'dash.locaux_geres': {fr:'Locaux gérés',en:'Managed units',rn:'Ivyumba bicungwa',sw:'Vyumba vinavyosimamiwa',rw:'Ibyumba bicungwa',it:'Unità gestite',es:'Locales gestionados',zh:'管理房间'},
  'dash.revenus_mois': {fr:'Revenus du mois',en:'Monthly revenue',rn:'Amafaranga y\'ukwezi',sw:'Mapato ya mwezi',rw:'Amafaranga y\'ukwezi',it:'Entrate del mese',es:'Ingresos del mes',zh:'本月收入'},
  'dash.charges_mois': {fr:'Charges du mois',en:'Monthly expenses',rn:'Amagarama y\'ukwezi',sw:'Gharama za mwezi',rw:'Ibiciro by\'ukwezi',it:'Spese del mese',es:'Gastos del mes',zh:'本月支出'},
  'dash.benefice_net': {fr:'Bénéfice net',en:'Net profit',rn:'Inyungu nyakuri',sw:'Faida halisi',rw:'Inyungu nyakuri',it:'Utile netto',es:'Beneficio neto',zh:'净利润'},
  'dash.bif_encaisses': {fr:'BIF encaissés',en:'BIF collected',rn:'BIF zinjiye',sw:'BIF zilizopokelewa',rw:'BIF zinjiye',it:'BIF incassati',es:'BIF cobrados',zh:'已收BIF'},
  'dash.total_depenses': {fr:'Total dépenses',en:'Total expenses',rn:'Amagarama yose',sw:'Jumla ya gharama',rw:'Igiteranyo cy\'ibiciro',it:'Totale spese',es:'Total de gastos',zh:'总支出'},
  'dash.encaissements_12m': {fr:'Encaissements 12 mois',en:'12-month collections',rn:'Ivyinjiye mu mezi 12',sw:'Makusanyo ya miezi 12',rw:'Ibyinjiye mu mezi 12',it:'Incassi 12 mesi',es:'Cobros en 12 meses',zh:'12个月收款'},
  'dash.revenus': {fr:'Revenus',en:'Revenue',rn:'Amafaranga',sw:'Mapato',rw:'Amafaranga',it:'Entrate',es:'Ingresos',zh:'收入'},
  'dash.charges': {fr:'Charges',en:'Expenses',rn:'Amagarama',sw:'Gharama',rw:'Ibiciro',it:'Spese',es:'Gastos',zh:'支出'},
  'dash.rappels_urgents': {fr:'Rappels urgents',en:'Urgent reminders',rn:'Icibutswa cihutirwa',sw:'Vikumbusho vya haraka',rw:'Kwibutsa byihutirwa',it:'Promemoria urgenti',es:'Recordatorios urgentes',zh:'紧急提醒'},
  'dash.aucun_rappel': {fr:'✅ Aucun rappel urgent',en:'✅ No urgent reminders',rn:'✅ Nta cibutswa',sw:'✅ Hakuna vikumbusho',rw:'✅ Nta kwibutswa',it:'✅ Nessun promemoria',es:'✅ Sin recordatorios',zh:'✅ 无紧急提醒'},
  'dash.taux_paiement': {fr:'Taux de paiement',en:'Payment rate',rn:'Igipimo c\'ivyishuwe',sw:'Kiwango cha malipo',rw:'Igipimo cy\'ubwishyu',it:'Tasso di pagamento',es:'Tasa de pago',zh:'付款率'},
  'dash.commission_cabinet': {fr:'Commission cabinet',en:'Agency commission',rn:'Komisiyo y\'ikigo',sw:'Kamisheni ya kampuni',rw:'Komisiyo y\'ikigo',it:'Commissione agenzia',es:'Comisión de la agencia',zh:'代理佣金'},
  'dash.sur_revenus_bruts': {fr:'sur revenus bruts',en:'on gross revenue',rn:'ku mafaranga yose',sw:'kwa mapato ghafi',rw:'ku mafaranga yose',it:'su ricavi lordi',es:'sobre ingresos brutos',zh:'占总收入'},
  'dash.payes': {fr:'payés',en:'paid',rn:'vyishuwe',sw:'vimelipwa',rw:'byishyuwe',it:'pagati',es:'pagados',zh:'已付'},
  'dash.en_retard': {fr:'en retard',en:'overdue',rn:'vyatevye',sw:'zimechelewa',rw:'byatinze',it:'in ritardo',es:'atrasados',zh:'逾期'},
  'dash.occupes': {fr:'occupés',en:'occupied',rn:'vyuzuye',sw:'vimejaa',rw:'byuzuye',it:'occupati',es:'ocupados',zh:'已占用'},
  'dash.libres': {fr:'libres',en:'vacant',rn:'vyubusa',sw:'wazi',rw:'byubusa',it:'liberi',es:'libres',zh:'空置'},

  // ── ACTIONS COMMUNES ───────────────────────────────────────────
  'common.rechercher': {fr:'Rechercher…',en:'Search…',rn:'Kurondera…',sw:'Tafuta…',rw:'Gushakisha…',it:'Cerca…',es:'Buscar…',zh:'搜索…'},
  'common.nouveau': {fr:'+ Nouveau',en:'+ New',rn:'+ Gishasha',sw:'+ Mpya',rw:'+ Gishya',it:'+ Nuovo',es:'+ Nuevo',zh:'+ 新建'},
  'common.actions': {fr:'Actions',en:'Actions',rn:'Ibikorwa',sw:'Vitendo',rw:'Ibikorwa',it:'Azioni',es:'Acciones',zh:'操作'},
  'common.enregistrer': {fr:'💾 Enregistrer',en:'💾 Save',rn:'💾 Kubika',sw:'💾 Hifadhi',rw:'💾 Bika',it:'💾 Salva',es:'💾 Guardar',zh:'💾 保存'},
  'common.annuler': {fr:'Annuler',en:'Cancel',rn:'Kureka',sw:'Ghairi',rw:'Kureka',it:'Annulla',es:'Cancelar',zh:'取消'},
  'common.fermer': {fr:'Fermer',en:'Close',rn:'Gufunga',sw:'Funga',rw:'Gufunga',it:'Chiudi',es:'Cerrar',zh:'关闭'},
  'common.supprimer': {fr:'🗑 Supprimer',en:'🗑 Delete',rn:'🗑 Gusiba',sw:'🗑 Futa',rw:'🗑 Siba',it:'🗑 Elimina',es:'🗑 Eliminar',zh:'🗑 删除'},
  'common.modifier': {fr:'Modifier',en:'Edit',rn:'Guhindura',sw:'Hariri',rw:'Hindura',it:'Modifica',es:'Editar',zh:'编辑'},
  'common.voir': {fr:'👁 Voir',en:'👁 View',rn:'👁 Kuraba',sw:'👁 Ona',rw:'👁 Reba',it:'👁 Vedi',es:'👁 Ver',zh:'👁 查看'},
  'common.chargement': {fr:'Chargement…',en:'Loading…',rn:'Biriko biratangurwa…',sw:'Inapakia…',rw:'Biratangira…',it:'Caricamento…',es:'Cargando…',zh:'加载中…'},
  'common.aucune_donnee': {fr:'Aucune donnée',en:'No data',rn:'Nta makuru',sw:'Hakuna data',rw:'Nta makuru',it:'Nessun dato',es:'Sin datos',zh:'无数据'},
  'common.erreur': {fr:'Erreur',en:'Error',rn:'Ikosa',sw:'Hitilafu',rw:'Ikosa',it:'Errore',es:'Error',zh:'错误'},
  'common.tous_statuts': {fr:'Tous statuts',en:'All statuses',rn:'Uko biri kwose',sw:'Hali zote',rw:'Uko bimeze kwose',it:'Tutti gli stati',es:'Todos los estados',zh:'所有状态'},

  // ── STATUTS / BADGES ───────────────────────────────────────────
  'status.paye': {fr:'Payé',en:'Paid',rn:'Vyishuwe',sw:'Imelipwa',rw:'Byishyuwe',it:'Pagato',es:'Pagado',zh:'已付款'},
  'status.retard': {fr:'En retard',en:'Overdue',rn:'Vyatevye',sw:'Imechelewa',rw:'Byatinze',it:'In ritardo',es:'Atrasado',zh:'逾期'},
  'status.attente': {fr:'En attente',en:'Pending',rn:'Bitegerezwa',sw:'Inasubiri',rw:'Bitegerejwe',it:'In attesa',es:'Pendiente',zh:'待处理'},
  'status.actif': {fr:'Actif',en:'Active',rn:'Kirakora',sw:'Hai',rw:'Bikora',it:'Attivo',es:'Activo',zh:'活跃'},
  'status.resilie': {fr:'Résilié',en:'Terminated',rn:'Vyahagaritswe',sw:'Imesitishwa',rw:'Byahagaritswe',it:'Risolto',es:'Rescindido',zh:'已终止'},
  'status.expire': {fr:'Expiré',en:'Expired',rn:'Vyarangiye',sw:'Imekwisha',rw:'Byarangiye',it:'Scaduto',es:'Vencido',zh:'已过期'},
  'status.partiel': {fr:'Partiel',en:'Partial',rn:'Igice',sw:'Sehemu',rw:'Igice',it:'Parziale',es:'Parcial',zh:'部分'},
  'status.libre': {fr:'Libre',en:'Vacant',rn:'Kirubusa',sw:'Wazi',rw:'Kirubusa',it:'Libero',es:'Libre',zh:'空置'},
  'status.occupe': {fr:'Occupé',en:'Occupied',rn:'Kirubuzuye',sw:'Imejaa',rw:'Kirubuzuye',it:'Occupato',es:'Ocupado',zh:'已占用'},
  'status.valide': {fr:'Validé',en:'Validated',rn:'Vyemejwe',sw:'Imethibitishwa',rw:'Byemejwe',it:'Convalidato',es:'Validado',zh:'已验证'},
  'status.rejete': {fr:'Rejeté',en:'Rejected',rn:'Vyanse',sw:'Imekataliwa',rw:'Byanze',it:'Rifiutato',es:'Rechazado',zh:'已拒绝'},

  // ── TABLE: PROPRIÉTAIRES ─────────────────────────────────────
  'th.nom_complet': {fr:'Nom complet',en:'Full name',rn:'Amazina yose',sw:'Jina kamili',rw:'Amazina yose',it:'Nome completo',es:'Nombre completo',zh:'全名'},
  'th.telephone': {fr:'Téléphone',en:'Phone',rn:'Terefone',sw:'Simu',rw:'Telefoni',it:'Telefono',es:'Teléfono',zh:'电话'},
  'th.email': {fr:'Email',en:'Email',rn:'Imeyili',sw:'Barua pepe',rw:'Imeyili',it:'Email',es:'Correo electrónico',zh:'电子邮件'},
  'th.province': {fr:'Province',en:'Province',rn:'Intara',sw:'Mkoa',rw:'Intara',it:'Provincia',es:'Provincia',zh:'省'},
  'th.commune': {fr:'Commune',en:'Commune',rn:'Umurenge',sw:'Wilaya',rw:'Umurenge',it:'Comune',es:'Municipio',zh:'区'},
  'th.quartier': {fr:'Quartier',en:'Neighborhood',rn:'Ikibare',sw:'Mtaa',rw:'Akagari',it:'Quartiere',es:'Barrio',zh:'街区'},

  // ── MODAL LABELS (formulaires) ─────────────────────────────────
  'form.nom_complet': {fr:'Nom complet *',en:'Full name *',rn:'Amazina yose *',sw:'Jina kamili *',rw:'Amazina yose *',it:'Nome completo *',es:'Nombre completo *',zh:'全名 *'},
  'form.telephone': {fr:'Téléphone',en:'Phone',rn:'Terefone',sw:'Simu',rw:'Telefoni',it:'Telefono',es:'Teléfono',zh:'电话'},
  'form.province': {fr:'Province',en:'Province',rn:'Intara',sw:'Mkoa',rw:'Intara',it:'Provincia',es:'Provincia',zh:'省'},
  'form.montant': {fr:'Montant (BIF) *',en:'Amount (BIF) *',rn:'Amafaranga (BIF) *',sw:'Kiasi (BIF) *',rw:'Amafaranga (BIF) *',it:'Importo (BIF) *',es:'Importe (BIF) *',zh:'金额 (BIF) *'},
  'form.date': {fr:'Date *',en:'Date *',rn:'Itariki *',sw:'Tarehe *',rw:'Itariki *',it:'Data *',es:'Fecha *',zh:'日期 *'},

  // ── PAGE TITLES (topbar dynamique) ─────────────────────────────
  'title.dashboard': {fr:'Tableau de bord',en:'Dashboard',rn:'Ikibaho',sw:'Dashibodi',rw:'Ikibaho',it:'Pannello',es:'Panel',zh:'仪表盘'},
  'title.proprietaires': {fr:'Propriétaires',en:'Owners',rn:'Abanyene',sw:'Wamiliki',rw:'Abanyirai',it:'Proprietari',es:'Propietarios',zh:'业主'},
  'title.immeubles': {fr:'Immeubles',en:'Buildings',rn:'Amazu',sw:'Majengo',rw:'Inyubako',it:'Edifici',es:'Edificios',zh:'楼宇'},
  'title.locaux': {fr:'Locaux',en:'Units',rn:'Ivyumba',sw:'Vyumba',rw:'Ibyumba',it:'Locali',es:'Locales',zh:'房间'},
  'title.locataires': {fr:'Locataires',en:'Tenants',rn:'Abakode',sw:'Wapangaji',rw:'Abakode',it:'Inquilini',es:'Inquilinos',zh:'租户'},
  'title.loyers': {fr:'Loyers & Paiements',en:'Rents & Payments',rn:'Amakodo n\'Ivyishuwe',sw:'Kodi na Malipo',rw:'Ubukode n\'Ubwishyu',it:'Affitti e Pagamenti',es:'Alquileres y Pagos',zh:'租金与付款'},
  'title.rapports': {fr:'Rapports',en:'Reports',rn:'Raporo',sw:'Ripoti',rw:'Raporo',it:'Report',es:'Informes',zh:'报告'},
  'title.utilisateurs': {fr:'Utilisateurs',en:'Users',rn:'Abakoresha',sw:'Watumiaji',rw:'Abakoresha',it:'Utenti',es:'Usuarios',zh:'用户'}
};

// ── MOTEUR ═══════════════════════════════════════════════════════
function t(key) {
  var lang = localStorage.getItem('appLang') || 'fr';
  var entry = I18N[key];
  if (!entry) return key;
  return entry[lang] || entry.fr || key;
}

function setLanguage(lang) {
  localStorage.setItem('appLang', lang);
  applyTranslations();
  // Recharge la section active pour retraduire le contenu généré en JS
  var activeNav = document.querySelector('.nav-item.active');
  var activeId = document.querySelector('.section.active')?.id?.replace('s-', '');
  if (activeId && typeof LOADERS !== 'undefined' && LOADERS[activeId]) {
    LOADERS[activeId]();
  }
  if (typeof loadDash === 'function' && activeId === 'dashboard') loadDash();
}

function applyTranslations() {
  document.querySelectorAll('[data-i18n]').forEach(function(el) {
    var key = el.getAttribute('data-i18n');
    el.textContent = t(key);
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {
    el.placeholder = t(el.getAttribute('data-i18n-placeholder'));
  });
  // Titre de page courant (si section connue)
  var activeId = document.querySelector('.section.active')?.id?.replace('s-', '');
  var titleKey = 'title.' + activeId;
  if (activeId && I18N[titleKey]) {
    document.getElementById('page-title').textContent = t(titleKey);
  }
}

function initLanguageSwitcher() {
  var saved = localStorage.getItem('appLang') || 'fr';
  var sel = document.getElementById('lang-select');
  if (!sel) return;
  sel.innerHTML = Object.keys(I18N_LANGS).map(function(code) {
    return '<option value="' + code + '"' + (code === saved ? ' selected' : '') + '>' + I18N_LANGS[code] + '</option>';
  }).join('');
  sel.value = saved;
  sel.addEventListener('change', function() { setLanguage(this.value); });
  applyTranslations();
}

document.addEventListener('DOMContentLoaded', initLanguageSwitcher);