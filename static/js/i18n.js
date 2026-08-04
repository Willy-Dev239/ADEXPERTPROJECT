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

  // ── COMMUN (compléments) ────────────────────────────────────────
  'common.tous': {fr:'Tous',en:'All',rn:'Vyose',sw:'Zote',rw:'Byose',it:'Tutti',es:'Todos',zh:'全部'},
  'common.tous_types': {fr:'Tous types',en:'All types',rn:'Ubwoko bwose',sw:'Aina zote',rw:'Ubwoko bwose',it:'Tutti i tipi',es:'Todos los tipos',zh:'所有类型'},
  'common.aucun_option': {fr:'-- Aucun --',en:'-- None --',rn:'-- Nta na kimwe --',sw:'-- Hakuna --',rw:'-- Nta na kimwe --',it:'-- Nessuno --',es:'-- Ninguno --',zh:'-- 无 --'},
  'common.impayes': {fr:'Impayés',en:'Unpaid',rn:'Ntibigashuwe',sw:'Hazijalipwa',rw:'Bidishyuwe',it:'Non pagati',es:'Impagados',zh:'未付款'},

  // ── EN-TÊTES DE TABLE (compléments) ─────────────────────────────
  'th.nom': {fr:'Nom',en:'Name',rn:'Izina',sw:'Jina',rw:'Izina',it:'Nome',es:'Nombre',zh:'名称'},
  'th.annee': {fr:'Année',en:'Year',rn:'Umwaka',sw:'Mwaka',rw:'Umwaka',it:'Anno',es:'Año',zh:'年份'},
  'th.infos': {fr:'Infos',en:'Info',rn:'Amakuru',sw:'Taarifa',rw:'Amakuru',it:'Info',es:'Info',zh:'信息'},
  'th.reference': {fr:'Référence',en:'Reference',rn:'Icapo',sw:'Marejeleo',rw:'Inomero',it:'Riferimento',es:'Referencia',zh:'参考号'},
  'th.proprietaire': {fr:'Propriétaire',en:'Owner',rn:'Umunyene',sw:'Mmiliki',rw:'Nyirai',it:'Proprietario',es:'Propietario',zh:'业主'},
  'th.immeuble': {fr:'Immeuble',en:'Building',rn:'Inzu',sw:'Jengo',rw:'Inyubako',it:'Edificio',es:'Edificio',zh:'楼宇'},
  'th.type': {fr:'Type',en:'Type',rn:'Ubwoko',sw:'Aina',rw:'Ubwoko',it:'Tipo',es:'Tipo',zh:'类型'},
  'th.adresse': {fr:'Adresse',en:'Address',rn:'Aderesi',sw:'Anwani',rw:'Aderesi',it:'Indirizzo',es:'Dirección',zh:'地址'},
  'th.surface': {fr:'Surface',en:'Area',rn:'Ubugari',sw:'Eneo',rw:'Ubuso',it:'Superficie',es:'Superficie',zh:'面积'},
  'th.meuble': {fr:'Meublé',en:'Furnished',rn:'Birimwo ibikoresho',sw:'Vimewekwa samani',rw:'Bifite ibikoresho',it:'Arredato',es:'Amueblado',zh:'已配家具'},
  'th.statut': {fr:'Statut',en:'Status',rn:'Uko biri',sw:'Hali',rw:'Uko bimeze',it:'Stato',es:'Estado',zh:'状态'},
  'th.nom_prenom': {fr:'Nom Prénom',en:'Full name',rn:'Izina n\'irindi',sw:'Jina kamili',rw:'Amazina',it:'Nome e cognome',es:'Nombre y apellido',zh:'姓名'},
  'th.local_actuel': {fr:'Local actuel',en:'Current unit',rn:'Icumba c\'ubu',sw:'Chumba cha sasa',rw:'Icyumba cyahoze',it:'Unità attuale',es:'Local actual',zh:'当前房间'},
  'th.situation': {fr:'Situation',en:'Status',rn:'Uko bimeze',sw:'Hali',rw:'Uko bimeze',it:'Situazione',es:'Situación',zh:'状况'},
  'th.numero_contrat': {fr:'N° Contrat',en:'Contract No.',rn:'Nomero y\'amasezerano',sw:'Na. Mkataba',rw:'Nomero y\'amasezerano',it:'N. Contratto',es:'N.º Contrato',zh:'合同编号'},
  'th.locataire': {fr:'Locataire',en:'Tenant',rn:'Umukode',sw:'Mpangaji',rw:'Umukode',it:'Inquilino',es:'Inquilino',zh:'租户'},
  'th.local': {fr:'Local',en:'Unit',rn:'Icumba',sw:'Chumba',rw:'Icyumba',it:'Locale',es:'Local',zh:'房间'},
  'th.entree': {fr:'Entrée',en:'Move-in',rn:'Injira',sw:'Kuingia',rw:'Kwinjira',it:'Ingresso',es:'Entrada',zh:'入住'},
  'th.loyer_hc': {fr:'Loyer HC',en:'Rent (excl. charges)',rn:'Ikodo (nta magarama)',sw:'Kodi (bila gharama)',rw:'Ubukode (nta biciro)',it:'Affitto (esclusi oneri)',es:'Alquiler (sin gastos)',zh:'租金(不含费用)'},
  'th.periodicite': {fr:'Périodicité',en:'Frequency',rn:'Rikagenda gute',sw:'Marudio',rw:'Uburyo bwo kwishyura',it:'Periodicità',es:'Periodicidad',zh:'周期'},
  'th.libelle': {fr:'Libellé',en:'Label',rn:'Izina ry\'ikiyago',sw:'Jina la malipo',rw:'Izina',it:'Descrizione',es:'Descripción',zh:'标签'},
  'th.total': {fr:'Total',en:'Total',rn:'Vyose',sw:'Jumla',rw:'Igiteranyo',it:'Totale',es:'Total',zh:'总计'},
  'th.solde': {fr:'Solde',en:'Balance',rn:'Amasigaye',sw:'Salio',rw:'Amasigaye',it:'Saldo',es:'Saldo',zh:'余额'},
  'th.echeance': {fr:'Échéance',en:'Due date',rn:'Igihe co kwishura',sw:'Tarehe ya mwisho',rw:'Igihe cyo kwishyura',it:'Scadenza',es:'Vencimiento',zh:'到期日'},
  'th.date': {fr:'Date',en:'Date',rn:'Itariki',sw:'Tarehe',rw:'Itariki',it:'Data',es:'Fecha',zh:'日期'},
  'th.notes': {fr:'Notes',en:'Notes',rn:'Inyandiko',sw:'Maelezo',rw:'Inyandiko',it:'Note',es:'Notas',zh:'备注'},
  'th.photo': {fr:'Photo',en:'Photo',rn:'Ifoto',sw:'Picha',rw:'Ifoto',it:'Foto',es:'Foto',zh:'照片'},
  'th.montant': {fr:'Montant',en:'Amount',rn:'Amafaranga',sw:'Kiasi',rw:'Amafaranga',it:'Importo',es:'Importe',zh:'金额'},
  'th.convention': {fr:'Convention',en:'Agreement',rn:'Amasezerano',sw:'Makubaliano',rw:'Amasezerano',it:'Convenzione',es:'Convenio',zh:'协议'},
  'th.banque': {fr:'Banque',en:'Bank',rn:'Ibanki',sw:'Benki',rw:'Banki',it:'Banca',es:'Banco',zh:'银行'},
  'th.date_virement': {fr:'Date virement',en:'Transfer date',rn:'Itariki yo kurungika',sw:'Tarehe ya uhamisho',rw:'Itariki y\'ubwishyu',it:'Data bonifico',es:'Fecha de transferencia',zh:'转账日期'},
  'th.justificatif': {fr:'Justificatif',en:'Proof',rn:'Icemezo',sw:'Uthibitisho',rw:'Icyemezo',it:'Giustificativo',es:'Justificante',zh:'凭证'},
  'th.utilisateur': {fr:'Utilisateur',en:'User',rn:'Umukoresha',sw:'Mtumiaji',rw:'Umukoresha',it:'Utente',es:'Usuario',zh:'用户'},
  'th.role': {fr:'Rôle',en:'Role',rn:'Uruhara',sw:'Jukumu',rw:'Uruhare',it:'Ruolo',es:'Rol',zh:'角色'},
  'th.actif': {fr:'Actif',en:'Active',rn:'Kirakora',sw:'Hai',rw:'Bikora',it:'Attivo',es:'Activo',zh:'活跃'},
  'th.inscription': {fr:'Inscription',en:'Joined',rn:'Yiyandikishije',sw:'Alijiunga',rw:'Yiyandikishije',it:'Iscritto',es:'Registrado',zh:'注册日期'},

  // ── SECTIONS (titres de carte spécifiques) ──────────────────────
  'sec.contrats_societe_titre': {fr:'Contrats Propriétaire ↔ Société',en:'Owner ↔ Company Contracts',rn:'Amasezerano Umunyene ↔ Isosiyete',sw:'Mikataba Mmiliki ↔ Kampuni',rw:'Amasezerano Nyirai ↔ Isosiyete',it:'Contratti Proprietario ↔ Società',es:'Contratos Propietario ↔ Empresa',zh:'业主↔公司合同'},
  'sec.charges': {fr:'Charges & Frais',en:'Expenses & Fees',rn:'Amagarama',sw:'Gharama na Ada',rw:'Ibiciro n\'Amafaranga',it:'Spese e Costi',es:'Gastos y Tarifas',zh:'费用与支出'},
  'sec.bordereaux_titre': {fr:'Bordereaux de paiement',en:'Payment slips',rn:'Impapuro z\'ivyishuwe',sw:'Risiti za malipo',rw:'Impapuro z\'ubwishyu',it:'Distinte di pagamento',es:'Comprobantes de pago',zh:'付款凭单'},
  'sec.virements_titre': {fr:'Bordereaux de virement propriétaires',en:'Owner transfer slips',rn:'Impapuro z\'ivyishuwe ku banyene',sw:'Risiti za uhamisho wa wamiliki',rw:'Impapuro z\'ubwishyu ku banyirai',it:'Distinte di bonifico proprietari',es:'Comprobantes de transferencia a propietarios',zh:'业主转账凭单'},
  'sec.stats_proprietaire': {fr:'Stats par propriétaire',en:'Stats by owner',rn:'Imibare ku munyene',sw:'Takwimu kwa mmiliki',rw:'Imibare ku nyirai',it:'Statistiche per proprietario',es:'Estadísticas por propietario',zh:'按业主统计'},
  'sec.creances': {fr:'Créances & Arriérés',en:'Receivables & Arrears',rn:'Imyenda itarishwa',sw:'Madeni yaliyochelewa',rw:'Imyenda itarishyuwe',it:'Crediti e Arretrati',es:'Cuentas por cobrar y atrasos',zh:'应收账款与欠款'},

  // ── BOUTONS SPÉCIFIQUES ──────────────────────────────────────────
  'btn.nouveau_contrat': {fr:'Nouveau contrat',en:'New contract',rn:'Amasezerano mashasha',sw:'Mkataba mpya',rw:'Amasezerano mashya',it:'Nuovo contratto',es:'Nuevo contrato',zh:'新合同'},
  'btn.nouveau_loyer': {fr:'Nouveau loyer',en:'New rent',rn:'Ikodo rishasha',sw:'Kodi mpya',rw:'Ubukode bushya',it:'Nuovo affitto',es:'Nuevo alquiler',zh:'新租金'},
  'btn.nouvelle_charge': {fr:'Nouvelle charge',en:'New expense',rn:'Igarama rishasha',sw:'Gharama mpya',rw:'Igiciro gishya',it:'Nuova spesa',es:'Nuevo gasto',zh:'新支出'},
  'btn.nouvel_utilisateur': {fr:'Nouvel utilisateur',en:'New user',rn:'Umukoresha mushasha',sw:'Mtumiaji mpya',rw:'Umukoresha mushya',it:'Nuovo utente',es:'Nuevo usuario',zh:'新用户'},
  'btn.envoyer_alerte': {fr:'Envoyer alerte',en:'Send alert',rn:'Kohereza icibutswa',sw:'Tuma tahadhari',rw:'Kohereza icyitonderwa',it:'Invia avviso',es:'Enviar alerta',zh:'发送提醒'},

  // ── ACCÈS REFUSÉ ──────────────────────────────────────────────────
  'acc.refuse_titre': {fr:'Accès refusé',en:'Access denied',rn:'Ntibyemewe kwinjira',sw:'Ufikiaji umekataliwa',rw:'Ntibyemewe kwinjira',it:'Accesso negato',es:'Acceso denegado',zh:'拒绝访问'},
  'acc.refuse_msg': {fr:'Réservé aux Administrateurs.',en:'Reserved for Administrators.',rn:'Bikwiye Abayobozi gusa.',sw:'Kwa Wasimamizi tu.',rw:'Bigenewe Abayobozi gusa.',it:'Riservato agli Amministratori.',es:'Reservado para Administradores.',zh:'仅限管理员。'},
  'info.role_lecteur_defaut': {fr:'Tout nouvel inscrit reçoit le rôle Lecteur par défaut.',en:'Every new user gets the Viewer role by default.',rn:'Uwiyandikishije wese aronka uruhara rw\'Umusomyi.',sw:'Kila mtumiaji mpya anapata jukumu la Msomaji kwa default.',rw:'Uwiyandikishije wese ahabwa uruhare rw\'Umusomyi.',it:'Ogni nuovo iscritto riceve il ruolo di Lettore per impostazione predefinita.',es:'Todo nuevo usuario recibe el rol de Lector de forma predeterminada.',zh:'每个新注册用户默认获得查看者角色。'},

  // ── CHAT ──────────────────────────────────────────────────────────
  'chat.groupes_titre': {fr:'Groupes par immeuble',en:'Groups by building',rn:'Amatsinda ku nzu',sw:'Vikundi kwa jengo',rw:'Amatsinda ku nyubako',it:'Gruppi per edificio',es:'Grupos por edificio',zh:'按楼宇分组'},
  'chat.select_prop': {fr:'— Sélectionner un propriétaire —',en:'— Select an owner —',rn:'— Hitamwo umunyene —',sw:'— Chagua mmiliki —',rw:'— Hitamo nyirai —',it:'— Seleziona un proprietario —',es:'— Seleccionar un propietario —',zh:'— 选择业主 —'},
  'chat.select_imm': {fr:'— Sélectionner un immeuble —',en:'— Select a building —',rn:'— Hitamwo inzu —',sw:'— Chagua jengo —',rw:'— Hitamo inyubako —',it:'— Seleziona un edificio —',es:'— Seleccionar un edificio —',zh:'— 选择楼宇 —'},
  'chat.ouvrir': {fr:'💬 Ouvrir le chat',en:'💬 Open chat',rn:'💬 Fungura ikiganiro',sw:'💬 Fungua mazungumzo',rw:'💬 Fungura ikiganiro',it:'💬 Apri chat',es:'💬 Abrir chat',zh:'💬 打开聊天'},
  'chat.tous_groupes': {fr:'Tous les groupes',en:'All groups',rn:'Amatsinda yose',sw:'Vikundi vyote',rw:'Amatsinda yose',it:'Tutti i gruppi',es:'Todos los grupos',zh:'所有群组'},
  'chat.select_groupe': {fr:'💬 Sélectionnez un groupe',en:'💬 Select a group',rn:'💬 Hitamwo itsinda',sw:'💬 Chagua kikundi',rw:'💬 Hitamo itsinda',it:'💬 Seleziona un gruppo',es:'💬 Selecciona un grupo',zh:'💬 选择群组'},
  'chat.select_groupe_msgs': {fr:'Sélectionnez un groupe pour voir les messages',en:'Select a group to see messages',rn:'Hitamwo itsinda kugira urabe ubutumwa',sw:'Chagua kikundi kuona ujumbe',rw:'Hitamo itsinda kugira ubone ubutumwa',it:'Seleziona un gruppo per vedere i messaggi',es:'Selecciona un grupo para ver los mensajes',zh:'选择群组查看消息'},
  'chat.ecrire_message': {fr:'Écrire un message…',en:'Write a message…',rn:'Andika ubutumwa…',sw:'Andika ujumbe…',rw:'Andika ubutumwa…',it:'Scrivi un messaggio…',es:'Escribe un mensaje…',zh:'输入消息…'},

  // ── PAGE TITLES (topbar dynamique) ─────────────────────────────
  'title.dashboard': {fr:'Tableau de bord',en:'Dashboard',rn:'Ikibaho',sw:'Dashibodi',rw:'Ikibaho',it:'Pannello',es:'Panel',zh:'仪表盘'},
  'title.proprietaires': {fr:'Propriétaires',en:'Owners',rn:'Abanyene',sw:'Wamiliki',rw:'Abanyirai',it:'Proprietari',es:'Propietarios',zh:'业主'},
  'title.immeubles': {fr:'Immeubles',en:'Buildings',rn:'Amazu',sw:'Majengo',rw:'Inyubako',it:'Edifici',es:'Edificios',zh:'楼宇'},
  'title.locaux': {fr:'Locaux',en:'Units',rn:'Ivyumba',sw:'Vyumba',rw:'Ibyumba',it:'Locali',es:'Locales',zh:'房间'},
  'title.locataires': {fr:'Locataires',en:'Tenants',rn:'Abakode',sw:'Wapangaji',rw:'Abakode',it:'Inquilini',es:'Inquilinos',zh:'租户'},
  'title.loyers': {fr:'Loyers & Paiements',en:'Rents & Payments',rn:'Amakodo n\'Ivyishuwe',sw:'Kodi na Malipo',rw:'Ubukode n\'Ubwishyu',it:'Affitti e Pagamenti',es:'Alquileres y Pagos',zh:'租金与付款'},
  'title.rapports': {fr:'Rapports',en:'Reports',rn:'Raporo',sw:'Ripoti',rw:'Raporo',it:'Report',es:'Informes',zh:'报告'},
  'title.utilisateurs': {fr:'Utilisateurs',en:'Users',rn:'Abakoresha',sw:'Watumiaji',rw:'Abakoresha',it:'Utenti',es:'Usuarios',zh:'用户'},
  'title.contrats_societe': {fr:'Contrats Société',en:'Company Contracts',rn:'Amasezerano y\'Isosiyete',sw:'Mikataba ya Kampuni',rw:'Amasezerano y\'Isosiyete',it:'Contratti Società',es:'Contratos de la Empresa',zh:'公司合同'},
  'title.charges': {fr:'Charges & Frais',en:'Expenses & Fees',rn:'Amagarama',sw:'Gharama na Ada',rw:'Ibiciro n\'Amafaranga',it:'Spese e Costi',es:'Gastos y Tarifas',zh:'费用与支出'},
  'title.bordereaux': {fr:'Bordereaux',en:'Payment Slips',rn:'Impapuro z\'ivyishuwe',sw:'Risiti za Malipo',rw:'Impapuro z\'ubwishyu',it:'Distinte',es:'Comprobantes',zh:'凭单'},
  'title.virements': {fr:'Virements Propriétaires',en:'Owner Transfers',rn:'Ivyishuwe ku Banyene',sw:'Uhamisho wa Wamiliki',rw:'Ubwishyu ku Banyirai',it:'Bonifici Proprietari',es:'Transferencias a Propietarios',zh:'业主转账'},
  'title.portefeuille': {fr:'Portefeuille cabinet',en:'Agency Portfolio',rn:'Igikoresho c\'ikigo',sw:'Kwingi wa kampuni',rw:'Icyegeranyo cy\'ikigo',it:'Portafoglio agenzia',es:'Cartera de la agencia',zh:'代理投资组合'},
  'title.chat': {fr:'Chat Immeubles',en:'Buildings Chat',rn:'Ikiganiro c\'amazu',sw:'Mazungumzo ya majengo',rw:'Ikiganiro cy\'inyubako',it:'Chat Edifici',es:'Chat de Edificios',zh:'楼宇聊天'},
  'title.notifications': {fr:'Notifications',en:'Notifications',rn:'Amamenyesha',sw:'Arifa',rw:'Amamenyesha',it:'Notifiche',es:'Notificaciones',zh:'通知'},

  // ── COMPLÉMENTS EN-TÊTES ─────────────────────────────────────────
  'th.paye': {fr:'Payé',en:'Paid',rn:'Vyishuwe',sw:'Imelipwa',rw:'Byishyuwe',it:'Pagato',es:'Pagado',zh:'已付'},
  'th.revenu_brut': {fr:'Revenu brut',en:'Gross revenue',rn:'Amafaranga yose',sw:'Mapato ghafi',rw:'Amafaranga yose',it:'Ricavo lordo',es:'Ingreso bruto',zh:'总收入'},
  'th.commission': {fr:'Commission',en:'Commission',rn:'Komisiyo',sw:'Kamisheni',rw:'Komisiyo',it:'Commissione',es:'Comisión',zh:'佣金'},
  'th.net_verse': {fr:'Net versé',en:'Net paid',rn:'Ivyatanzwe vy\'ukuri',sw:'Iliyolipwa halisi',rw:'Ibyatanzwe by\'ukuri',it:'Netto versato',es:'Neto pagado',zh:'实付净额'},

  // ── OPTIONS DE FORMULAIRE ─────────────────────────────────────────
  'opt.appartement': {fr:'Appartement',en:'Apartment',rn:'Apartima',sw:'Ghorofa',rw:'Apartima',it:'Appartamento',es:'Apartamento',zh:'公寓'},
  'opt.maison': {fr:'Maison',en:'House',rn:'Inzu',sw:'Nyumba',rw:'Inzu',it:'Casa',es:'Casa',zh:'住宅'},
  'opt.bureau': {fr:'Bureau',en:'Office',rn:'Ibiro',sw:'Ofisi',rw:'Ibiro',it:'Ufficio',es:'Oficina',zh:'办公室'},
  'opt.commerce': {fr:'Commerce',en:'Shop',rn:'Ubudandaji',sw:'Duka',rw:'Ubucuruzi',it:'Negozio',es:'Comercio',zh:'商铺'},
  'opt.garage': {fr:'Garage',en:'Garage',rn:'Garaje',sw:'Karakana',rw:'Garaje',it:'Garage',es:'Garaje',zh:'车库'},
  'opt.autre': {fr:'Autre',en:'Other',rn:'Ikindi',sw:'Nyingine',rw:'Ikindi',it:'Altro',es:'Otro',zh:'其他'},
  'opt.non': {fr:'Non',en:'No',rn:'Oya',sw:'Hapana',rw:'Oya',it:'No',es:'No',zh:'否'},
  'opt.oui': {fr:'Oui',en:'Yes',rn:'Ego',sw:'Ndiyo',rw:'Yego',it:'Sì',es:'Sí',zh:'是'},
  'opt.mensuel': {fr:'Mensuel',en:'Monthly',rn:'Buri kwezi',sw:'Kila mwezi',rw:'Buri kwezi',it:'Mensile',es:'Mensual',zh:'每月'},
  'opt.bimensuel': {fr:'Bi-mensuel',en:'Bi-monthly',rn:'Buri mezi abiri',sw:'Kila miezi miwili',rw:'Buri mezi abiri',it:'Bimestrale',es:'Bimensual',zh:'每两月'},
  'opt.trimestriel': {fr:'Trimestriel',en:'Quarterly',rn:'Buri mezi atatu',sw:'Kila robo mwaka',rw:'Buri mezi atatu',it:'Trimestrale',es:'Trimestral',zh:'每季度'},
  'opt.semestriel': {fr:'Semestriel',en:'Half-yearly',rn:'Buri mezi atandatu',sw:'Kila nusu mwaka',rw:'Buri mezi atandatu',it:'Semestrale',es:'Semestral',zh:'每半年'},
  'opt.annuel': {fr:'Annuel',en:'Yearly',rn:'Buri mwaka',sw:'Kila mwaka',rw:'Buri mwaka',it:'Annuale',es:'Anual',zh:'每年'},
  'opt.especes': {fr:'💵 Espèces',en:'💵 Cash',rn:'💵 Amahera y\'intoke',sw:'💵 Fedha taslimu',rw:'💵 Amafaranga',it:'💵 Contanti',es:'💵 Efectivo',zh:'💵 现金'},
  'opt.virement': {fr:'🏦 Virement',en:'🏦 Bank transfer',rn:'🏦 Ivyishuwe vy\'ibanki',sw:'🏦 Uhamisho wa benki',rw:'🏦 Ubwishyu bwa banki',it:'🏦 Bonifico',es:'🏦 Transferencia',zh:'🏦 银行转账'},
  'opt.cheque': {fr:'📝 Chèque',en:'📝 Check',rn:'📝 Ceke',sw:'📝 Hundi',rw:'📝 Ceke',it:'📝 Assegno',es:'📝 Cheque',zh:'📝 支票'},
  'opt.mobile_money': {fr:'📱 Mobile Money',en:'📱 Mobile Money',rn:'📱 Mobile Money',sw:'📱 Pesa za Simu',rw:'📱 Mobile Money',it:'📱 Mobile Money',es:'📱 Dinero Móvil',zh:'📱 移动支付'},
  'opt.travaux': {fr:'Travaux/Entretien',en:'Repairs/Maintenance',rn:'Ibikorwa/Ugusana',sw:'Ukarabati/Matengenezo',rw:'Imirimo/Kubungabunga',it:'Lavori/Manutenzione',es:'Obras/Mantenimiento',zh:'维修/保养'},
  'opt.impot_locatif': {fr:'Impôt locatif',en:'Rental tax',rn:'Ikoli y\'ikodo',sw:'Kodi ya upangaji',rw:'Umusoro w\'ubukode',it:'Imposta di locazione',es:'Impuesto de alquiler',zh:'租赁税'},
  'opt.impot_foncier': {fr:'Taxe foncière',en:'Property tax',rn:'Ikoli y\'itongo',sw:'Kodi ya mali',rw:'Umusoro w\'umutungo',it:'Imposta fondiaria',es:'Impuesto predial',zh:'房产税'},
  'opt.frais_cabinet': {fr:'Frais cabinet',en:'Agency fee',rn:'Amagarama y\'ikigo',sw:'Ada za kampuni',rw:'Amafaranga y\'ikigo',it:'Costi agenzia',es:'Comisión de agencia',zh:'代理费'},
  'opt.assurance': {fr:'Assurance',en:'Insurance',rn:'Ubwishingizi',sw:'Bima',rw:'Ubwishingizi',it:'Assicurazione',es:'Seguro',zh:'保险'},
  'opt.eau_electricite': {fr:'Eau/Électricité',en:'Water/Electricity',rn:'Amazi/Umuriro',sw:'Maji/Umeme',rw:'Amazi/Amashanyarazi',it:'Acqua/Elettricità',es:'Agua/Electricidad',zh:'水电'},
  'opt.tous_locataires': {fr:'📢 Tous les locataires',en:'📢 All tenants',rn:'📢 Abakode bose',sw:'📢 Wapangaji wote',rw:'📢 Abakode bose',it:'📢 Tutti gli inquilini',es:'📢 Todos los inquilinos',zh:'📢 所有租户'},
  'opt.alerte_generale': {fr:'⚠️ Alerte générale',en:'⚠️ General alert',rn:'⚠️ Icibutswa rusangi',sw:'⚠️ Tahadhari ya jumla',rw:'⚠️ Icyitonderwa rusange',it:'⚠️ Avviso generale',es:'⚠️ Alerta general',zh:'⚠️ 一般提醒'},
  'opt.rappel_paiement': {fr:'💰 Rappel paiement',en:'💰 Payment reminder',rn:'💰 Icibutswa c\'ivyishuwe',sw:'💰 Ukumbusho wa malipo',rw:'💰 Kwibutsa ubwishyu',it:'💰 Promemoria pagamento',es:'💰 Recordatorio de pago',zh:'💰 付款提醒'},
  'opt.maintenance': {fr:'🔧 Maintenance',en:'🔧 Maintenance',rn:'🔧 Ugusana',sw:'🔧 Matengenezo',rw:'🔧 Kubungabunga',it:'🔧 Manutenzione',es:'🔧 Mantenimiento',zh:'🔧 维护'},
  'opt.info': {fr:'ℹ️ Information',en:'ℹ️ Information',rn:'ℹ️ Amakuru',sw:'ℹ️ Taarifa',rw:'ℹ️ Amakuru',it:'ℹ️ Informazione',es:'ℹ️ Información',zh:'ℹ️ 信息'},
  'role.locataire': {fr:'🏠 Locataire',en:'🏠 Tenant',rn:'🏠 Umukode',sw:'🏠 Mpangaji',rw:'🏠 Umukode',it:'🏠 Inquilino',es:'🏠 Inquilino',zh:'🏠 租户'},
  'role.proprietaire': {fr:'🤝 Propriétaire',en:'🤝 Owner',rn:'🤝 Umunyene',sw:'🤝 Mmiliki',rw:'🤝 Nyirai',it:'🤝 Proprietario',es:'🤝 Propietario',zh:'🤝 业主'},

  // ── RAPPORTS (cartes) ─────────────────────────────────────────────
  'rap.mensuel_loyers': {fr:'Rapport mensuel loyers',en:'Monthly rent report',rn:'Raporo y\'ukwezi y\'amakodo',sw:'Ripoti ya kila mwezi ya kodi',rw:'Raporo y\'ukwezi y\'ubukode',it:'Report mensile affitti',es:'Informe mensual de alquileres',zh:'月度租金报告'},
  'rap.taux_impayes': {fr:'Taux paiement, impayés',en:'Payment rate, unpaid',rn:'Igipimo c\'ivyishuwe, ivitishuwe',sw:'Kiwango cha malipo, hazijalipwa',rw:'Igipimo cy\'ubwishyu, bidishyuwe',it:'Tasso pagamento, non pagati',es:'Tasa de pago, impagados',zh:'付款率、未付款'},
  'rap.mensuel_charges': {fr:'Rapport mensuel charges',en:'Monthly expense report',rn:'Raporo y\'ukwezi y\'amagarama',sw:'Ripoti ya kila mwezi ya gharama',rw:'Raporo y\'ukwezi y\'ibiciro',it:'Report mensile spese',es:'Informe mensual de gastos',zh:'月度支出报告'},
  'rap.repartition_type': {fr:'Répartition par type',en:'Breakdown by type',rn:'Igabura ku bwoko',sw:'Mgawanyo kwa aina',rw:'Igabana ku bwoko',it:'Ripartizione per tipo',es:'Desglose por tipo',zh:'按类型细分'},
  'rap.journalier': {fr:'Rapport journalier',en:'Daily report',rn:'Raporo ya buri musi',sw:'Ripoti ya kila siku',rw:'Raporo ya buri munsi',it:'Report giornaliero',es:'Informe diario',zh:'每日报告'},
  'rap.encaissements_jour': {fr:'Encaissements du jour',en:'Today\'s collections',rn:'Ivyinjiye vy\'umusi',sw:'Makusanyo ya siku',rw:'Ibyinjiye by\'umunsi',it:'Incassi del giorno',es:'Cobros del día',zh:'当日收款'},

  // ── PORTEFEUILLE ────────────────────────────────────────────────
  'pf.commission9': {fr:'Commission (9%)',en:'Commission (9%)',rn:'Komisiyo (9%)',sw:'Kamisheni (9%)',rw:'Komisiyo (9%)',it:'Commissione (9%)',es:'Comisión (9%)',zh:'佣金 (9%)'},
  'pf.geres': {fr:'Gérés',en:'Managed',rn:'Bicungwa',sw:'Inayosimamiwa',rw:'Bicungwa',it:'Gestiti',es:'Gestionados',zh:'已管理'},
  'pf.loyers_anticipes': {fr:'Loyers anticipés',en:'Advance rents',rn:'Amakodo yaratanzwe imbere',sw:'Kodi za mapema',rw:'Ubukode bwatanzwe mbere',it:'Affitti anticipati',es:'Alquileres anticipados',zh:'预付租金'},
  'pf.dossiers': {fr:'Dossiers',en:'Cases',rn:'Amadosiye',sw:'Faili',rw:'Amadosiye',it:'Pratiche',es:'Expedientes',zh:'案例'},
  'pf.creances': {fr:'Créances',en:'Receivables',rn:'Imyenda',sw:'Madeni',rw:'Imyenda',it:'Crediti',es:'Cuentas por cobrar',zh:'应收账款'},
  'pf.arrieres': {fr:'Arriérés',en:'Arrears',rn:'Imyenda itarishwa',sw:'Madeni yaliyochelewa',rw:'Imyenda itarishyuwe',it:'Arretrati',es:'Atrasos',zh:'欠款'},

  // ── NOTIFICATIONS (carte) ───────────────────────────────────────
  'notif.titre': {fr:'🔔 Notifications & Alertes locataires',en:'🔔 Tenant Notifications & Alerts',rn:'🔔 Amamenyesha n\'Ivyibutswa ku bakode',sw:'🔔 Arifa na Tahadhari za Wapangaji',rw:'🔔 Amamenyesha n\'Ibyitonderwa by\'abakode',it:'🔔 Notifiche e Avvisi Inquilini',es:'🔔 Notificaciones y Alertas de Inquilinos',zh:'🔔 租户通知与提醒'},

  // ── MODALS : titres & sous-titres ────────────────────────────────
  'modal.rappels_titre': {fr:'Rappels urgents',en:'Urgent reminders',rn:'Icibutswa cihutirwa',sw:'Vikumbusho vya haraka',rw:'Kwibutsa byihutirwa',it:'Promemoria urgenti',es:'Recordatorios urgentes',zh:'紧急提醒'},
  'modal.actions_requises': {fr:'Actions requises',en:'Actions required',rn:'Ibikorwa bikenewe',sw:'Vitendo vinavyohitajika',rw:'Ibikorwa bikenewe',it:'Azioni richieste',es:'Acciones requeridas',zh:'需要采取的行动'},
  'modal.nouveau_proprietaire': {fr:'Nouveau propriétaire',en:'New owner',rn:'Umunyene mushasha',sw:'Mmiliki mpya',rw:'Nyirai mushya',it:'Nuovo proprietario',es:'Nuevo propietario',zh:'新业主'},
  'modal.info_proprietaire': {fr:'Informations du propriétaire',en:'Owner information',rn:'Amakuru y\'umunyene',sw:'Taarifa za mmiliki',rw:'Amakuru y\'nyirai',it:'Informazioni proprietario',es:'Información del propietario',zh:'业主信息'},
  'modal.nouvel_immeuble': {fr:'Nouvel immeuble',en:'New building',rn:'Inzu nshasha',sw:'Jengo jipya',rw:'Inyubako nshya',it:'Nuovo edificio',es:'Nuevo edificio',zh:'新楼宇'},
  'modal.info_immeuble': {fr:'Informations sur l\'immeuble',en:'Building information',rn:'Amakuru ku nzu',sw:'Taarifa za jengo',rw:'Amakuru ku nyubako',it:'Informazioni edificio',es:'Información del edificio',zh:'楼宇信息'},
  'modal.nouveau_local': {fr:'Nouveau local',en:'New unit',rn:'Icumba gishasha',sw:'Chumba kipya',rw:'Icyumba gishya',it:'Nuova unità',es:'Nuevo local',zh:'新房间'},
  'modal.bien_immobilier': {fr:'Bien immobilier',en:'Real estate unit',rn:'Ivyaguzwe',sw:'Mali isiyohamishika',rw:'Umutungo utimukanwa',it:'Bene immobiliare',es:'Bien inmobiliario',zh:'房产'},
  'modal.nouveau_locataire': {fr:'Nouveau locataire',en:'New tenant',rn:'Umukode mushasha',sw:'Mpangaji mpya',rw:'Umukode mushya',it:'Nuovo inquilino',es:'Nuevo inquilino',zh:'新租户'},
  'modal.info_locataire': {fr:'Informations du locataire',en:'Tenant information',rn:'Amakuru y\'umukode',sw:'Taarifa za mpangaji',rw:'Amakuru y\'umukode',it:'Informazioni inquilino',es:'Información del inquilino',zh:'租户信息'},
  'modal.nouveau_contrat_titre': {fr:'Nouveau contrat',en:'New contract',rn:'Amasezerano mashasha',sw:'Mkataba mpya',rw:'Amasezerano mashya',it:'Nuovo contratto',es:'Nuevo contrato',zh:'新合同'},
  'modal.contrat_location': {fr:'Contrat de location',en:'Lease contract',rn:'Amasezerano yo gukodesha',sw:'Mkataba wa kukodisha',rw:'Amasezerano yo gukodesha',it:'Contratto di locazione',es:'Contrato de alquiler',zh:'租赁合同'},
  'modal.generer_loyers': {fr:'Générer les loyers',en:'Generate rents',rn:'Kurema amakodo',sw:'Tengeneza kodi',rw:'Kurema ubukode',it:'Genera affitti',es:'Generar alquileres',zh:'生成租金'},
  'modal.generation_auto': {fr:'Génération automatique',en:'Automatic generation',rn:'Ukwikorera',sw:'Uzalishaji wa kiotomatiki',rw:'Gukora byikoresha',it:'Generazione automatica',es:'Generación automática',zh:'自动生成'},
  'modal.nouveau_loyer_titre': {fr:'Nouveau loyer',en:'New rent',rn:'Ikodo rishasha',sw:'Kodi mpya',rw:'Ubukode bushya',it:'Nuovo affitto',es:'Nuevo alquiler',zh:'新租金'},
  'modal.saisie_manuelle': {fr:'Saisie manuelle',en:'Manual entry',rn:'Kwandika ku ntoke',sw:'Uingizaji wa mkono',rw:'Kwinjiza ku ntoki',it:'Inserimento manuale',es:'Entrada manual',zh:'手动录入'},
  'modal.enregistrer_paiement': {fr:'Enregistrer un paiement',en:'Record a payment',rn:'Kwandika ivyishuwe',sw:'Rekodi malipo',rw:'Kwandika ubwishyu',it:'Registra un pagamento',es:'Registrar un pago',zh:'记录付款'},
  'modal.saisir_reglement': {fr:'Saisir le règlement du locataire',en:'Enter tenant payment',rn:'Andika ivyishuwe vy\'umukode',sw:'Ingiza malipo ya mpangaji',rw:'Andika ubwishyu bw\'umukode',it:'Inserisci il pagamento dell\'inquilino',es:'Ingresar el pago del inquilino',zh:'输入租户付款'},
  'modal.quittance_titre': {fr:'Quittance de loyer',en:'Rent receipt',rn:'Icemezo c\'ikodo',sw:'Risiti ya kodi',rw:'Icyemezo cy\'ubukode',it:'Ricevuta d\'affitto',es:'Recibo de alquiler',zh:'租金收据'},
  'modal.doc_officiel': {fr:'Document officiel',en:'Official document',rn:'Inyandiko ya reta',sw:'Hati rasmi',rw:'Inyandiko yemewe',it:'Documento ufficiale',es:'Documento oficial',zh:'官方文件'},
  'modal.nouvelle_charge_titre': {fr:'Nouvelle charge',en:'New expense',rn:'Igarama rishasha',sw:'Gharama mpya',rw:'Igiciro gishya',it:'Nuova spesa',es:'Nuevo gasto',zh:'新支出'},
  'modal.depense_liee': {fr:'Dépense liée à un bien',en:'Expense linked to a property',rn:'Igarama rifitanye n\'ivyaguzwe',sw:'Gharama inayohusiana na mali',rw:'Igiciro gifitanye isano n\'umutungo',it:'Spesa legata a un immobile',es:'Gasto relacionado con un bien',zh:'与房产相关的支出'},
  'modal.rapport': {fr:'Rapport',en:'Report',rn:'Raporo',sw:'Ripoti',rw:'Raporo',it:'Report',es:'Informe',zh:'报告'},
  'modal.statistiques': {fr:'Statistiques',en:'Statistics',rn:'Imibare',sw:'Takwimu',rw:'Imibare',it:'Statistiche',es:'Estadísticas',zh:'统计数据'},
  'modal.nouvel_utilisateur_titre': {fr:'Nouvel utilisateur',en:'New user',rn:'Umukoresha mushasha',sw:'Mtumiaji mpya',rw:'Umukoresha mushya',it:'Nuovo utente',es:'Nuevo usuario',zh:'新用户'},
  'modal.gestion_acces': {fr:'Gestion des accès',en:'Access management',rn:'Ubuyobozi bw\'uburenganzira',sw:'Usimamizi wa ufikiaji',rw:'Ubuyobozi bw\'uburenganzira',it:'Gestione accessi',es:'Gestión de accesos',zh:'权限管理'},
  'modal.envoyer_alerte_titre': {fr:'Envoyer une alerte locataire',en:'Send a tenant alert',rn:'Kohereza icibutswa ku mukode',sw:'Tuma tahadhari kwa mpangaji',rw:'Kohereza icyitonderwa ku mukode',it:'Invia un avviso all\'inquilino',es:'Enviar una alerta al inquilino',zh:'向租户发送提醒'},
  'modal.notif_vers': {fr:'Notification vers un ou tous les locataires',en:'Notification to one or all tenants',rn:'Amamenyesha ku mukode umwe canke bose',sw:'Arifa kwa mpangaji mmoja au wote',rw:'Amamenyesha ku mukode umwe cyangwa bose',it:'Notifica a uno o tutti gli inquilini',es:'Notificación a uno o todos los inquilinos',zh:'向一个或所有租户发送通知'},
  'modal.valider_bordereau': {fr:'Valider le bordereau',en:'Validate the slip',rn:'Kwemeza urupapuro',sw:'Thibitisha risiti',rw:'Kwemeza urupapuro',it:'Convalida la distinta',es:'Validar el comprobante',zh:'验证凭单'},
  'modal.verif_justificatif': {fr:'Vérification du justificatif de paiement',en:'Payment proof verification',rn:'Kwemeza icemezo c\'ivyishuwe',sw:'Uthibitisho wa uthibitisho wa malipo',rw:'Kugenzura icyemezo cy\'ubwishyu',it:'Verifica della prova di pagamento',es:'Verificación del comprobante de pago',zh:'付款凭证核实'},
  'modal.valider_virement': {fr:'Valider le virement',en:'Validate the transfer',rn:'Kwemeza ivyishuwe',sw:'Thibitisha uhamisho',rw:'Kwemeza ubwishyu',it:'Convalida il bonifico',es:'Validar la transferencia',zh:'验证转账'},
  'modal.verif_justificatif_bancaire': {fr:'Vérification du justificatif bancaire',en:'Bank proof verification',rn:'Kwemeza icemezo c\'ibanki',sw:'Uthibitisho wa hati ya benki',rw:'Kugenzura icyemezo cya banki',it:'Verifica della prova bancaria',es:'Verificación del comprobante bancario',zh:'银行凭证核实'},
  'modal.nouveau_contrat_societe': {fr:'Nouveau contrat société',en:'New company contract',rn:'Amasezerano mashasha y\'isosiyete',sw:'Mkataba mpya wa kampuni',rw:'Amasezerano mashya y\'isosiyete',it:'Nuovo contratto società',es:'Nuevo contrato de empresa',zh:'新公司合同'},
  'modal.convention_gestion': {fr:'Convention de gestion locative — ADEXPER',en:'Property management agreement — ADEXPER',rn:'Amasezerano yo gucunga — ADEXPER',sw:'Makubaliano ya usimamizi — ADEXPER',rw:'Amasezerano yo gucunga — ADEXPER',it:'Accordo di gestione locativa — ADEXPER',es:'Convenio de gestión de alquileres — ADEXPER',zh:'物业管理协议 — ADEXPER'},
  'modal.apercu_contrat_titre': {fr:'Aperçu du contrat',en:'Contract preview',rn:'Kuraba amasezerano',sw:'Muhtasari wa mkataba',rw:'Kureba amasezerano',it:'Anteprima contratto',es:'Vista previa del contrato',zh:'合同预览'},

  // ── MODALS : champs de formulaire ────────────────────────────────
  'form.lier_compte': {fr:'Lier à un compte utilisateur',en:'Link to a user account',rn:'Kwifatanya n\'ukoreshwa',sw:'Unganisha na akaunti ya mtumiaji',rw:'Guhuza n\'ukoresha',it:'Collega a un account utente',es:'Vincular a una cuenta de usuario',zh:'关联用户账户'},
  'form.select_user_opt': {fr:'— Sélectionner un utilisateur (optionnel) —',en:'— Select a user (optional) —',rn:'— Hitamwo umukoresha (bidasabwa) —',sw:'— Chagua mtumiaji (hiari) —',rw:'— Hitamo umukoresha (bitegetswe) —',it:'— Seleziona un utente (opzionale) —',es:'— Seleccionar un usuario (opcional) —',zh:'— 选择用户（可选）—'},
  'info.liaison_auto_prop': {fr:'Choisir un utilisateur créera automatiquement la liaison avec ce propriétaire.',en:'Choosing a user will automatically link them to this owner.',rn:'Guhitamwo umukoresha bizoteza ivyifatanya n\'uyu munyene ku bwikorezi.',sw:'Kuchagua mtumiaji kutaunganisha kiotomatiki na mmiliki huyu.',rw:'Guhitamo umukoresha bizahuza ubwikorezi n\'uyu nyirai.',it:'Selezionando un utente verrà collegato automaticamente a questo proprietario.',es:'Elegir un usuario lo vinculará automáticamente con este propietario.',zh:'选择用户将自动与该业主关联。'},
  'info.liaison_auto_loca': {fr:'Choisir un utilisateur créera automatiquement la liaison avec ce locataire.',en:'Choosing a user will automatically link them to this tenant.',rn:'Guhitamwo umukoresha bizoteza ivyifatanya n\'uyu mukode ku bwikorezi.',sw:'Kuchagua mtumiaji kutaunganisha kiotomatiki na mpangaji huyu.',rw:'Guhitamo umukoresha bizahuza ubwikorezi n\'uyu mukode.',it:'Selezionando un utente verrà collegato automaticamente a questo inquilino.',es:'Elegir un usuario lo vinculará automáticamente con este inquilino.',zh:'选择用户将自动与该租户关联。'},
  'form.informations_complementaires': {fr:'Informations complémentaires',en:'Additional information',rn:'Amakuru arenga',sw:'Taarifa za ziada',rw:'Amakuru yongeweho',it:'Informazioni aggiuntive',es:'Información adicional',zh:'补充信息'},
  'form.nom_immeuble': {fr:'Nom de l\'immeuble *',en:'Building name *',rn:'Izina ry\'inzu *',sw:'Jina la jengo *',rw:'Izina ry\'inyubako *',it:'Nome dell\'edificio *',es:'Nombre del edificio *',zh:'楼宇名称 *'},
  'form.annee_construction': {fr:'Année de construction',en:'Year built',rn:'Umwaka waranguwe',sw:'Mwaka wa ujenzi',rw:'Umwaka wubatswe',it:'Anno di costruzione',es:'Año de construcción',zh:'建造年份'},
  'form.reference_star': {fr:'Référence *',en:'Reference *',rn:'Icapo *',sw:'Marejeleo *',rw:'Inomero *',it:'Riferimento *',es:'Referencia *',zh:'参考号 *'},
  'form.type_star': {fr:'Type *',en:'Type *',rn:'Ubwoko *',sw:'Aina *',rw:'Ubwoko *',it:'Tipo *',es:'Tipo *',zh:'类型 *'},
  'form.proprietaire_star': {fr:'Propriétaire *',en:'Owner *',rn:'Umunyene *',sw:'Mmiliki *',rw:'Nyirai *',it:'Proprietario *',es:'Propietario *',zh:'业主 *'},
  'form.superficie': {fr:'Superficie (m²)',en:'Area (m²)',rn:'Ubugari (m²)',sw:'Eneo (m²)',rw:'Ubuso (m²)',it:'Superficie (m²)',es:'Superficie (m²)',zh:'面积 (m²)'},
  'form.meuble': {fr:'Meublé',en:'Furnished',rn:'Birimwo ibikoresho',sw:'Vimewekwa samani',rw:'Bifite ibikoresho',it:'Arredato',es:'Amueblado',zh:'已配家具'},
  'form.nom_prenom_star': {fr:'Nom et Prénom *',en:'Full name *',rn:'Izina n\'irindi *',sw:'Jina kamili *',rw:'Amazina yose *',it:'Nome e cognome *',es:'Nombre y apellido *',zh:'姓名 *'},
  'form.adresse_postale': {fr:'Adresse postale',en:'Postal address',rn:'Aderesi yo kuposta',sw:'Anwani ya posta',rw:'Aderesi ya posita',it:'Indirizzo postale',es:'Dirección postal',zh:'邮寄地址'},
  'sit.financiere': {fr:'📊 Situation financière',en:'📊 Financial status',rn:'📊 Uko amafaranga ameze',sw:'📊 Hali ya kifedha',rw:'📊 Uko amafaranga ameze',it:'📊 Situazione finanziaria',es:'📊 Situación financiera',zh:'📊 财务状况'},
  'sit.total_loyers': {fr:'Total loyers',en:'Total rent',rn:'Amakodo yose',sw:'Jumla ya kodi',rw:'Igiteranyo cy\'ubukode',it:'Totale affitti',es:'Total de alquileres',zh:'总租金'},
  'btn.voir_historique': {fr:'📋 Voir l\'historique complet',en:'📋 View full history',rn:'📋 Kuraba amateka yose',sw:'📋 Ona historia kamili',rw:'📋 Reba amateka yose',it:'📋 Vedi cronologia completa',es:'📋 Ver historial completo',zh:'📋 查看完整历史'},
  'form.statut': {fr:'Statut',en:'Status',rn:'Uko biri',sw:'Hali',rw:'Uko bimeze',it:'Stato',es:'Estado',zh:'状态'},
  'form.locataire_star': {fr:'Locataire *',en:'Tenant *',rn:'Umukode *',sw:'Mpangaji *',rw:'Umukode *',it:'Inquilino *',es:'Inquilino *',zh:'租户 *'},
  'form.local_star': {fr:'Local *',en:'Unit *',rn:'Icumba *',sw:'Chumba *',rw:'Icyumba *',it:'Locale *',es:'Local *',zh:'房间 *'},
  'form.loyer_hc_star': {fr:'Loyer HC (BIF) *',en:'Rent excl. charges (BIF) *',rn:'Ikodo (nta magarama) (BIF) *',sw:'Kodi bila gharama (BIF) *',rw:'Ubukode (nta biciro) (BIF) *',it:'Affitto escl. oneri (BIF) *',es:'Alquiler sin gastos (BIF) *',zh:'租金(不含费用) (BIF) *'},
  'form.provisions_charges': {fr:'Provisions charges (BIF)',en:'Charge provisions (BIF)',rn:'Amagarama y\'imbere (BIF)',sw:'Akiba za gharama (BIF)',rw:'Ibiciro biteganyijwe (BIF)',it:'Accantonamenti oneri (BIF)',es:'Provisión de gastos (BIF)',zh:'费用预留 (BIF)'},
  'form.periodicite': {fr:'Périodicité',en:'Frequency',rn:'Rikagenda gute',sw:'Marudio',rw:'Uburyo bwo kwishyura',it:'Periodicità',es:'Periodicidad',zh:'周期'},
  'form.depot_garantie': {fr:'Dépôt de garantie (BIF)',en:'Security deposit (BIF)',rn:'Amahera y\'ingwati (BIF)',sw:'Amana ya dhamana (BIF)',rw:'Amafaranga y\'ingwate (BIF)',it:'Deposito cauzionale (BIF)',es:'Depósito de garantía (BIF)',zh:'押金 (BIF)'},
  'form.date_entree_star': {fr:'Date d\'entrée *',en:'Move-in date *',rn:'Itariki yo kwinjira *',sw:'Tarehe ya kuingia *',rw:'Itariki yo kwinjira *',it:'Data di ingresso *',es:'Fecha de entrada *',zh:'入住日期 *'},
  'form.date_sortie': {fr:'Date de sortie',en:'Move-out date',rn:'Itariki yo gusohoka',sw:'Tarehe ya kutoka',rw:'Itariki yo gusohoka',it:'Data di uscita',es:'Fecha de salida',zh:'退租日期'},
  'btn.resilier': {fr:'⚠️ Résilier',en:'⚠️ Terminate',rn:'⚠️ Kuhagarika',sw:'⚠️ Sitisha',rw:'⚠️ Kureka',it:'⚠️ Risolvi',es:'⚠️ Rescindir',zh:'⚠️ 终止'},
  'btn.generer_loyers': {fr:'⚡ Générer loyers',en:'⚡ Generate rents',rn:'⚡ Kurema amakodo',sw:'⚡ Tengeneza kodi',rw:'⚡ Kurema ubukode',it:'⚡ Genera affitti',es:'⚡ Generar alquileres',zh:'⚡ 生成租金'},
  'form.nb_mois': {fr:'Nombre de mois',en:'Number of months',rn:'Umubare w\'amezi',sw:'Idadi ya miezi',rw:'Umubare w\'amezi',it:'Numero di mesi',es:'Número de meses',zh:'月数'},
  'form.a_partir_du': {fr:'À partir du',en:'Starting from',rn:'Guhera ku',sw:'Kuanzia',rw:'Guhera ku',it:'A partire dal',es:'A partir del',zh:'起始于'},
  'info.loyers_non_dupliques': {fr:'Les loyers existants ne seront pas dupliqués.',en:'Existing rents will not be duplicated.',rn:'Amakodo asanzwe ntazosubirwamwo.',sw:'Kodi zilizopo hazitarudufishwa.',rw:'Ubukode busanzweho ntibuzasubirwamo.',it:'Gli affitti esistenti non verranno duplicati.',es:'Los alquileres existentes no se duplicarán.',zh:'现有租金不会重复生成。'},
  'btn.generer': {fr:'⚡ Générer',en:'⚡ Generate',rn:'⚡ Kurema',sw:'⚡ Tengeneza',rw:'⚡ Kurema',it:'⚡ Genera',es:'⚡ Generar',zh:'⚡ 生成'},
  'form.libelle_star': {fr:'Libellé *',en:'Label *',rn:'Izina *',sw:'Jina *',rw:'Izina *',it:'Descrizione *',es:'Descripción *',zh:'标签 *'},
  'form.contrat_associe': {fr:'Contrat associé',en:'Associated contract',rn:'Amasezerano afitanye isano',sw:'Mkataba unaohusiana',rw:'Amasezerano ahujwe',it:'Contratto associato',es:'Contrato asociado',zh:'关联合同'},
  'form.periode_du_star': {fr:'Période du *',en:'Period from *',rn:'Igihe guhera *',sw:'Kipindi kuanzia *',rw:'Igihe guhera *',it:'Periodo dal *',es:'Período desde *',zh:'期间起 *'},
  'form.periode_au': {fr:'Période au',en:'Period to',rn:'Igihe kugeza',sw:'Kipindi hadi',rw:'Igihe kugeza',it:'Periodo al',es:'Período hasta',zh:'期间止'},
  'form.charges_bif': {fr:'Charges (BIF)',en:'Charges (BIF)',rn:'Amagarama (BIF)',sw:'Gharama (BIF)',rw:'Ibiciro (BIF)',it:'Oneri (BIF)',es:'Gastos (BIF)',zh:'费用 (BIF)'},
  'form.echeance_star': {fr:'Échéance *',en:'Due date *',rn:'Igihe co kwishura *',sw:'Tarehe ya mwisho *',rw:'Igihe cyo kwishyura *',it:'Scadenza *',es:'Vencimiento *',zh:'到期日 *'},
  'form.notes': {fr:'Notes',en:'Notes',rn:'Inyandiko',sw:'Maelezo',rw:'Inyandiko',it:'Note',es:'Notas',zh:'备注'},
  'form.mode_paiement': {fr:'Mode de paiement',en:'Payment method',rn:'Uburyo bwo kwishura',sw:'Njia ya malipo',rw:'Uburyo bwo kwishyura',it:'Metodo di pagamento',es:'Método de pago',zh:'付款方式'},
  'form.reference_cheque': {fr:'Référence / N° chèque',en:'Reference / Check No.',rn:'Icapo / Nomero ya ceke',sw:'Marejeleo / Na. ya hundi',rw:'Inomero / Nomero ya ceke',it:'Riferimento / N. assegno',es:'Referencia / N.º de cheque',zh:'参考号/支票号'},
  'btn.valider_paiement': {fr:'✅ Valider le paiement',en:'✅ Confirm payment',rn:'✅ Kwemeza ivyishuwe',sw:'✅ Thibitisha malipo',rw:'✅ Kwemeza ubwishyu',it:'✅ Conferma pagamento',es:'✅ Confirmar pago',zh:'✅ 确认付款'},
  'btn.imprimer_pdf': {fr:'🖨️ Imprimer / PDF',en:'🖨️ Print / PDF',rn:'🖨️ Gucapa / PDF',sw:'🖨️ Chapisha / PDF',rw:'🖨️ Gucapa / PDF',it:'🖨️ Stampa / PDF',es:'🖨️ Imprimir / PDF',zh:'🖨️ 打印/PDF'},
  'form.libelle_desc': {fr:'Description de la dépense',en:'Expense description',rn:'Ibisobanuro vy\'igarama',sw:'Maelezo ya gharama',rw:'Ibisobanuro by\'igiciro',it:'Descrizione della spesa',es:'Descripción del gasto',zh:'支出描述'},
  'form.montant_ttc': {fr:'Montant TTC (BIF) *',en:'Total amount (BIF) *',rn:'Amafaranga yose (BIF) *',sw:'Kiasi jumla (BIF) *',rw:'Amafaranga yose (BIF) *',it:'Importo totale (BIF) *',es:'Importe total (BIF) *',zh:'总金额 (BIF) *'},
  'btn.telecharger': {fr:'⬇️ Télécharger',en:'⬇️ Download',rn:'⬇️ Kuramwo',sw:'⬇️ Pakua',rw:'⬇️ Kwakura',it:'⬇️ Scarica',es:'⬇️ Descargar',zh:'⬇️ 下载'},
  'form.prenom': {fr:'Prénom',en:'First name',rn:'Izina ryo hasi',sw:'Jina la kwanza',rw:'Izina',it:'Nome',es:'Nombre',zh:'名字'},
  'form.nom': {fr:'Nom',en:'Last name',rn:'Izina ryo hejuru',sw:'Jina la ukoo',rw:'Izina ry\'umuryango',it:'Cognome',es:'Apellido',zh:'姓氏'},
  'form.username_star': {fr:'Nom d\'utilisateur *',en:'Username *',rn:'Izina ry\'ukoreshwa *',sw:'Jina la mtumiaji *',rw:'Izina ry\'ukoresha *',it:'Nome utente *',es:'Nombre de usuario *',zh:'用户名 *'},
  'form.lier_profil': {fr:'Lier à un profil',en:'Link to a profile',rn:'Kwifatanya n\'umwirondoro',sw:'Unganisha na wasifu',rw:'Guhuza n\'umwirondoro',it:'Collega a un profilo',es:'Vincular a un perfil',zh:'关联档案'},
  'form.select_generique': {fr:'— Sélectionner —',en:'— Select —',rn:'— Hitamwo —',sw:'— Chagua —',rw:'— Hitamo —',it:'— Seleziona —',es:'— Seleccionar —',zh:'— 选择 —'},
  'form.mdp_star': {fr:'Mot de passe *',en:'Password *',rn:'Ijambo ry\'ibanga *',sw:'Nenosiri *',rw:'Ijambo ry\'ibanga *',it:'Password *',es:'Contraseña *',zh:'密码 *'},
  'form.destinataire': {fr:'Destinataire',en:'Recipient',rn:'Uwakira',sw:'Mpokeaji',rw:'Uwakira',it:'Destinatario',es:'Destinatario',zh:'收件人'},
  'form.titre_star': {fr:'Titre *',en:'Title *',rn:'Umutwe *',sw:'Kichwa *',rw:'Umutwe *',it:'Titolo *',es:'Título *',zh:'标题 *'},
  'form.message_star': {fr:'Message *',en:'Message *',rn:'Ubutumwa *',sw:'Ujumbe *',rw:'Ubutumwa *',it:'Messaggio *',es:'Mensaje *',zh:'消息 *'},
  'form.type_alerte': {fr:'Type d\'alerte',en:'Alert type',rn:'Ubwoko bw\'icibutswa',sw:'Aina ya tahadhari',rw:'Ubwoko bw\'icyitonderwa',it:'Tipo di avviso',es:'Tipo de alerta',zh:'提醒类型'},
  'btn.envoyer': {fr:'📤 Envoyer',en:'📤 Send',rn:'📤 Kohereza',sw:'📤 Tuma',rw:'📤 Kohereza',it:'📤 Invia',es:'📤 Enviar',zh:'📤 发送'},
  'form.commentaire_opt': {fr:'Commentaire (optionnel)',en:'Comment (optional)',rn:'Icivugo (bidasabwa)',sw:'Maoni (hiari)',rw:'Icyo utekereza (bitegetswe)',it:'Commento (opzionale)',es:'Comentario (opcional)',zh:'备注（可选）'},
  'btn.rejeter': {fr:'❌ Rejeter',en:'❌ Reject',rn:'❌ Kwanka',sw:'❌ Kataa',rw:'❌ Kwanga',it:'❌ Rifiuta',es:'❌ Rechazar',zh:'❌ 拒绝'},
  'btn.valider': {fr:'✅ Valider',en:'✅ Confirm',rn:'✅ Kwemeza',sw:'✅ Thibitisha',rw:'✅ Kwemeza',it:'✅ Conferma',es:'✅ Confirmar',zh:'✅ 确认'},
  'form.date_signature_star': {fr:'Date de signature *',en:'Signing date *',rn:'Itariki yo kuvyemeza *',sw:'Tarehe ya kusaini *',rw:'Itariki yo gusinya *',it:'Data di firma *',es:'Fecha de firma *',zh:'签署日期 *'},
  'form.date_effet_star': {fr:'Date d\'effet *',en:'Effective date *',rn:'Itariki itangura gukora *',sw:'Tarehe ya kuanza kutumika *',rw:'Itariki itangira gukora *',it:'Data di decorrenza *',es:'Fecha de vigencia *',zh:'生效日期 *'},
  'form.date_expiration': {fr:'Date d\'expiration',en:'Expiration date',rn:'Itariki yo kurangira',sw:'Tarehe ya mwisho',rw:'Itariki yo kurangira',it:'Data di scadenza',es:'Fecha de vencimiento',zh:'到期日期'},
  'form.taux_commission_star': {fr:'Taux de commission (%) *',en:'Commission rate (%) *',rn:'Igipimo ca komisiyo (%) *',sw:'Kiwango cha kamisheni (%) *',rw:'Igipimo cya komisiyo (%) *',it:'Tasso di commissione (%) *',es:'Tasa de comisión (%) *',zh:'佣金比例 (%) *'},
  'form.periodicite_reversement': {fr:'Périodicité de reversement',en:'Payout frequency',rn:'Rikagenda gute mu gutanga',sw:'Marudio ya malipo',rw:'Uburyo bwo gutanga',it:'Periodicità di versamento',es:'Periodicidad de pago',zh:'付款周期'},
  'form.frais_entree': {fr:'Frais d\'entrée (BIF)',en:'Entry fee (BIF)',rn:'Amagarama yo kwinjira (BIF)',sw:'Ada za kuingia (BIF)',rw:'Amafaranga yo kwinjira (BIF)',it:'Costi di ingresso (BIF)',es:'Cuota de entrada (BIF)',zh:'入场费 (BIF)'},
  'sec.conditions_financieres': {fr:'📋 Conditions financières',en:'📋 Financial terms',rn:'📋 Ibisabwa vy\'amahera',sw:'📋 Masharti ya kifedha',rw:'📋 Amabwiriza y\'amafaranga',it:'📋 Condizioni finanziarie',es:'📋 Condiciones financieras',zh:'📋 财务条款'},
  'sec.services_inclus': {fr:'📜 Services inclus',en:'📜 Included services',rn:'📜 Serivisi zirimwo',sw:'📜 Huduma zilizojumuishwa',rw:'📜 Serivisi zirimo',it:'📜 Servizi inclusi',es:'📜 Servicios incluidos',zh:'📜 包含服务'},
  'form.clauses': {fr:'Clauses particulières',en:'Special clauses',rn:'Ingingo zidasanzwe',sw:'Vipengele maalum',rw:'Ingingo zidasanzwe',it:'Clausole particolari',es:'Cláusulas especiales',zh:'特殊条款'},
  'form.notes_internes': {fr:'Notes internes',en:'Internal notes',rn:'Inyandiko zo mu nda',sw:'Maelezo ya ndani',rw:'Inyandiko z\'imbere',it:'Note interne',es:'Notas internas',zh:'内部备注'},
  'btn.apercu_contrat': {fr:'🖨️ Aperçu contrat',en:'🖨️ Contract preview',rn:'🖨️ Kuraba amasezerano',sw:'🖨️ Muhtasari wa mkataba',rw:'🖨️ Kureba amasezerano',it:'🖨️ Anteprima contratto',es:'🖨️ Vista previa del contrato',zh:'🖨️ 合同预览'},

  // ── COMPLÉMENT FINAL (sections restantes) ────────────────────────
  'title.contrats': {fr:'Contrats Location',en:'Lease Contracts',rn:'Amasezerano yo Gukodesha',sw:'Mikataba ya Kukodisha',rw:'Amasezerano yo Gukodesha',it:'Contratti di Locazione',es:'Contratos de Alquiler',zh:'租赁合同'},
  'common.nouveau_contrat': {fr:'+ Nouveau contrat',en:'+ New contract',rn:'+ Amasezerano mashasha',sw:'+ Mkataba mpya',rw:'+ Amasezerano mashya',it:'+ Nuovo contratto',es:'+ Nuevo contrato',zh:'+ 新合同'},
  'common.nouveau_loyer': {fr:'+ Nouveau loyer',en:'+ New rent',rn:'+ Ikodo gishasha',sw:'+ Kodi mpya',rw:'+ Ubukode bushya',it:'+ Nuovo affitto',es:'+ Nuevo alquiler',zh:'+ 新租金'},
  'common.nouvelle_charge': {fr:'+ Nouvelle charge',en:'+ New expense',rn:'+ Igarama rishasha',sw:'+ Gharama mpya',rw:'+ Igiciro gishya',it:'+ Nuova spesa',es:'+ Nuevo gasto',zh:'+ 新支出'},
  'common.nouvel_utilisateur': {fr:'+ Nouvel utilisateur',en:'+ New user',rn:'+ Uwukoresha mushasha',sw:'+ Mtumiaji mpya',rw:'+ Ukoresha mushya',it:'+ Nuovo utente',es:'+ Nuevo usuario',zh:'+ 新用户'},
  'common.envoyer_alerte': {fr:'+ Envoyer alerte',en:'+ Send alert',rn:'+ Rungika ikimenyesha',sw:'+ Tuma tahadhari',rw:'+ Ohereza umuburo',it:'+ Invia avviso',es:'+ Enviar alerta',zh:'+ 发送提醒'},
  'common.acces_refuse': {fr:'Accès refusé',en:'Access denied',rn:'Uburenganzira bwanse',sw:'Hairuhusiwi',rw:'Ntabwo wemerewe',it:'Accesso negato',es:'Acceso denegado',zh:'拒绝访问'},
  'common.reserve_admin': {fr:'Réservé aux Administrateurs.',en:'Reserved for Administrators.',rn:'Vyabuzwa Abayobozi gusa.',sw:'Kwa Wasimamizi tu.',rw:'Byemewe Abayobozi gusa.',it:'Riservato agli Amministratori.',es:'Reservado para Administradores.',zh:'仅限管理员。'},
  'chat.selectionner_prop': {fr:'— Sélectionner un propriétaire —',en:'— Select an owner —',rn:'— Hitamwo umunyene —',sw:'— Chagua mmiliki —',rw:'— Hitamo umunyirai —',it:'— Seleziona un proprietario —',es:'— Seleccionar un propietario —',zh:'— 选择业主 —'},
  'chat.selectionner_imm': {fr:'— Sélectionner un immeuble —',en:'— Select a building —',rn:'— Hitamwo inzu —',sw:'— Chagua jengo —',rw:'— Hitamo inyubako —',it:'— Seleziona un edificio —',es:'— Seleccionar un edificio —',zh:'— 选择楼宇 —'},
  'chat.selectionnez_groupe': {fr:'💬 Sélectionnez un groupe',en:'💬 Select a group',rn:'💬 Hitamwo ikundi',sw:'💬 Chagua kikundi',rw:'💬 Hitamo itsinda',it:'💬 Seleziona un gruppo',es:'💬 Selecciona un grupo',zh:'💬 选择群组'},
  'chat.selectionnez_pour_msgs': {fr:'Sélectionnez un groupe pour voir les messages',en:'Select a group to see messages',rn:'Hitamwo ikundi kugira urabe ubutumwa',sw:'Chagua kikundi kuona ujumbe',rw:'Hitamo itsinda kugira ubone ubutumwa',it:'Seleziona un gruppo per vedere i messaggi',es:'Selecciona un grupo para ver los mensajes',zh:'选择群组以查看消息'},
  'card.contrats_societe_title': {fr:'Contrats Propriétaire ↔ Société',en:'Owner ↔ Agency Contracts',rn:'Amasezerano Umunyene ↔ Isosiyete',sw:'Mikataba Mmiliki ↔ Kampuni',rw:'Amasezerano Umunyirai ↔ Isosiyete',it:'Contratti Proprietario ↔ Agenzia',es:'Contratos Propietario ↔ Agencia',zh:'业主↔代理合同'},
  'card.bordereaux_title': {fr:'Bordereaux de paiement',en:'Payment Slips',rn:'Impapuro z\'ivyishuwe',sw:'Risiti za Malipo',rw:'Impapuro z\'ubwishyu',it:'Distinte di pagamento',es:'Comprobantes de pago',zh:'付款凭单'},
  'card.virements_title': {fr:'Bordereaux de virement propriétaires',en:'Owner Transfer Slips',rn:'Impapuro z\'ivyishuwe ku banyene',sw:'Risiti za uhamisho wa wamiliki',rw:'Impapuro z\'ubwishyu ku banyirai',it:'Distinte bonifico proprietari',es:'Comprobantes de transferencia a propietarios',zh:'业主转账凭单'},
  'card.notifications_title': {fr:'Notifications & Alertes locataires',en:'Tenant Notifications & Alerts',rn:'Amamenyesha ku bakode',sw:'Arifa kwa Wapangaji',rw:'Amamenyesha ku bakode',it:'Notifiche e Avvisi inquilini',es:'Notificaciones y Alertas de inquilinos',zh:'租户通知与提醒'},
  'card.chat_groupes': {fr:'Groupes par immeuble',en:'Groups by building',rn:'Amakundi ku nzu',sw:'Vikundi kwa jengo',rw:'Amatsinda ku nyubako',it:'Gruppi per edificio',es:'Grupos por edificio',zh:'按楼宇分组'},
  'card.gestion_utilisateurs': {fr:'Gestion des utilisateurs',en:'User management',rn:'Ubuyobozi bw\'abakoresha',sw:'Usimamizi wa watumiaji',rw:'Ubuyobozi bw\'abakoresha',it:'Gestione utenti',es:'Gestión de usuarios',zh:'用户管理'},
  'form.infos_comp': {fr:'Informations complémentaires',en:'Additional information',rn:'Andi makuru',sw:'Taarifa za ziada',rw:'Andi makuru',it:'Informazioni aggiuntive',es:'Información adicional',zh:'附加信息'},
  'form.selectionner_user_opt': {fr:'— Sélectionner un utilisateur (optionnel) —',en:'— Select a user (optional) —',rn:'— Hitamwo uwukoresha (bidasabwa) —',sw:'— Chagua mtumiaji (si lazima) —',rw:'— Hitamo ukoresha (ntibisabwa) —',it:'— Seleziona un utente (opzionale) —',es:'— Seleccionar un usuario (opcional) —',zh:'— 选择用户(可选) —'}
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