-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2026 at 12:27 PM
-- Server version: 11.7.2-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `adexpert_recouvrement_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('87b4472e2b1ee30a19a9b849592757dd2efc366c', '2026-07-24 09:28:16.363574', 1),
('f10eb04e07c50888400d967cd5abe5910a678643', '2026-07-05 12:47:14.942000', 2);

-- --------------------------------------------------------

--
-- Table structure for table `auth_app_user`
--

CREATE TABLE `auth_app_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL DEFAULT 0,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL DEFAULT 0,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(20) NOT NULL DEFAULT 'lecteur',
  `telephone` varchar(30) NOT NULL,
  `locataire_profile_id` bigint(20) DEFAULT NULL,
  `proprietaire_profile_id` bigint(20) DEFAULT NULL
) ;

--
-- Dumping data for table `auth_app_user`
--

INSERT INTO `auth_app_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `role`, `telephone`, `locataire_profile_id`, `proprietaire_profile_id`) VALUES
(1, 'pbkdf2_sha256$600000$ORTYYp5g08q1VIraIzRQFK$HPVbl4MTCVSseAOgfegeMaWsCSKBHGQCE+/m7k+uPQ8=', '2026-05-09 19:18:31.164000', 1, 'admin', 'Admin', 'Systeme', 'admin@infinityhome.bi', 1, 1, '2026-05-09 19:06:25.630000', 'admin', '', NULL, NULL),
(2, 'pbkdf2_sha256$600000$9gHf7Zw7rMPFExsUxw3SWX$ccCU5KpqlrYtG17n6phDReXnkeIX8pKIi6MtYPH1h3M=', NULL, 0, 'gestionnaire1', 'Marie', 'HAKIZIMANA', 'gest@infinityhome.bi', 0, 1, '2026-05-09 19:06:26.634000', 'gestionnaire', '', NULL, NULL),
(3, 'pbkdf2_sha256$600000$4l34jdZdOHREPLqcIOwUaB$DclRoTHadWSm/Bd1h5mrIlrCh23PbCeMYWJPc2lG8bQ=', NULL, 0, 'proprietaire1', 'Jean Pierre', 'NKURUNZIZA', 'prop@email.com', 0, 1, '2026-05-09 19:06:27.571000', 'proprietaire', '', NULL, 1),
(4, 'pbkdf2_sha256$600000$5kDqimskg5tRjz5Q05M4V2$JBn30O5jmYqU9AGTEFKgZHBPNLNJlGdZh9IfmevDxI4=', NULL, 0, 'locataire1', 'Patrick', 'HABIMANA', 'patrick@email.com', 0, 1, '2026-05-09 19:06:28.703000', 'locataire', '', 1, NULL),
(5, 'pbkdf2_sha256$600000$bdoWVlYBidY0TYxXQHRIKc$gLJkIi0lC3Hk2WojXWo8VnhLx7GGB+rHgnfd8XQ6rN4=', NULL, 0, 'supportADE', '', '', 'support@ade.bi', 1, 1, '2026-05-09 19:16:05.219000', 'lecteur', '', NULL, NULL),
(6, 'pbkdf2_sha256$600000$S8GM26VhsmrMzmSQ4TWfPO$//UkiQDQKLyxb4OniyB2ghLi1onRtBROAaq4ScILQk0=', NULL, 0, 'Willy', 'Willy', 'Kabura', 'nyamitw@gmail.com', 0, 1, '2026-05-10 14:54:51.389000', 'lecteur', '67000988', NULL, NULL),
(7, 'pbkdf2_sha256$600000$B7AZmdqFHuPaj4bToF0NNp$uzUa+ljbyijQ3jW35OX6+RQ7XPJ0lFFxK7W0iHkisyw=', NULL, 0, 'kabura', 'Gerard', 'Kabura', 'kabura@gmail.com', 0, 1, '2026-05-10 14:56:26.359000', 'gestionnaire', '', NULL, NULL),
(8, 'pbkdf2_sha256$600000$7tWt16qSeBuStHlNRtjqIn$T5WqEerWg+OwSACrrp8iMFAD6DRHj/iuIYl8pLnt7tM=', NULL, 0, 'diella', 'Diella', 'keza', '', 0, 1, '2026-05-10 15:17:51.833000', 'gestionnaire', '', NULL, NULL),
(9, 'pbkdf2_sha256$600000$WH7dvoSdweCajVpzxVppxj$zNLzgXaHbtR9qejeeneuuKwbB77q67s7UO/1tGZ+kxY=', NULL, 0, 'MarcIIII', 'Keza', 'Jeanine', '', 0, 1, '2026-05-14 15:11:05.635000', 'locataire', '', 2, NULL),
(10, 'pbkdf2_sha256$600000$tZ0Ej2IBuFu9778G2wliGG$b695eCwVKTwMx2COZhUbmRa06HcFp6XO12zPBE0Slws=', NULL, 0, 'JohnKarikurubu', 'John', 'Karikurubu', '', 0, 1, '2026-05-26 08:10:01.570000', 'lecteur', '', NULL, NULL),
(11, 'pbkdf2_sha256$600000$OD35Yxrfl21kGJo7l7sGZL$icS1BChwfgmuOoJhNFPp9RA/T6YsNXuzLl8JLQS8LKs=', NULL, 0, 'niyuru', 'Willy', 'Niyuru', 'w@gmail.com', 0, 1, '2026-05-26 08:21:14.212000', 'proprietaire', '', NULL, 2),
(12, 'pbkdf2_sha256$600000$NIZ604ZGiAkj6HOVyFE73G$ijM6So6rR3zHu9RKh75b1rYwFPWlawT8wbaH0IsBfvE=', NULL, 0, 'Wallace', 'Wallace', 'Rukundo', 'walla@gmail.com', 0, 1, '2026-05-28 09:30:37.334000', 'lecteur', '', NULL, NULL),
(14, 'pbkdf2_sha256$600000$LqPEGb9LzZYG5FcnQdjqAd$J/64KXYDsJ9PIjBWg/ehyYDITugDRgR1Ww9p7yQfWFU=', NULL, 0, 'hilaire', 'Hilaire', 'Ngenzebuhoro', 'hilaire@gmail.com', 0, 1, '2026-06-03 10:26:36.177000', 'locataire', '', 5, 4);

-- --------------------------------------------------------

--
-- Table structure for table `auth_app_user_groups`
--

CREATE TABLE `auth_app_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_app_user_user_permissions`
--

CREATE TABLE `auth_app_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can view permission', 1, 'view_permission'),
(5, 'Can add group', 2, 'add_group'),
(6, 'Can change group', 2, 'change_group'),
(7, 'Can delete group', 2, 'delete_group'),
(8, 'Can view group', 2, 'view_group'),
(9, 'Can add content type', 3, 'add_contenttype'),
(10, 'Can change content type', 3, 'change_contenttype'),
(11, 'Can delete content type', 3, 'delete_contenttype'),
(12, 'Can view content type', 3, 'view_contenttype'),
(13, 'Can add Utilisateur', 4, 'add_user'),
(14, 'Can change Utilisateur', 4, 'change_user'),
(15, 'Can delete Utilisateur', 4, 'delete_user'),
(16, 'Can view Utilisateur', 4, 'view_user'),
(17, 'Can add Propriétaire', 5, 'add_proprietaire'),
(18, 'Can change Propriétaire', 5, 'change_proprietaire'),
(19, 'Can delete Propriétaire', 5, 'delete_proprietaire'),
(20, 'Can view Propriétaire', 5, 'view_proprietaire'),
(21, 'Can add Locataire', 6, 'add_locataire'),
(22, 'Can change Locataire', 6, 'change_locataire'),
(23, 'Can delete Locataire', 6, 'delete_locataire'),
(24, 'Can view Locataire', 6, 'view_locataire'),
(25, 'Can add log entry', 7, 'add_logentry'),
(26, 'Can change log entry', 7, 'change_logentry'),
(27, 'Can delete log entry', 7, 'delete_logentry'),
(28, 'Can view log entry', 7, 'view_logentry'),
(29, 'Can add session', 8, 'add_session'),
(30, 'Can change session', 8, 'change_session'),
(31, 'Can delete session', 8, 'delete_session'),
(32, 'Can view session', 8, 'view_session'),
(33, 'Can add Token', 9, 'add_token'),
(34, 'Can change Token', 9, 'change_token'),
(35, 'Can delete Token', 9, 'delete_token'),
(36, 'Can view Token', 9, 'view_token'),
(37, 'Can add token', 10, 'add_tokenproxy'),
(38, 'Can change token', 10, 'change_tokenproxy'),
(39, 'Can delete token', 10, 'delete_tokenproxy'),
(40, 'Can view token', 10, 'view_tokenproxy'),
(41, 'Can add Immeuble', 11, 'add_immeuble'),
(42, 'Can change Immeuble', 11, 'change_immeuble'),
(43, 'Can delete Immeuble', 11, 'delete_immeuble'),
(44, 'Can view Immeuble', 11, 'view_immeuble'),
(45, 'Can add Local', 12, 'add_local'),
(46, 'Can change Local', 12, 'change_local'),
(47, 'Can delete Local', 12, 'delete_local'),
(48, 'Can view Local', 12, 'view_local'),
(49, 'Can add Contrat Société', 13, 'add_contratsociete'),
(50, 'Can change Contrat Société', 13, 'change_contratsociete'),
(51, 'Can delete Contrat Société', 13, 'delete_contratsociete'),
(52, 'Can view Contrat Société', 13, 'view_contratsociete'),
(53, 'Can add Contrat', 14, 'add_contrat'),
(54, 'Can change Contrat', 14, 'change_contrat'),
(55, 'Can delete Contrat', 14, 'delete_contrat'),
(56, 'Can view Contrat', 14, 'view_contrat'),
(57, 'Can add Loyer', 15, 'add_loyer'),
(58, 'Can change Loyer', 15, 'change_loyer'),
(59, 'Can delete Loyer', 15, 'delete_loyer'),
(60, 'Can view Loyer', 15, 'view_loyer'),
(61, 'Can add paiement', 16, 'add_paiement'),
(62, 'Can change paiement', 16, 'change_paiement'),
(63, 'Can delete paiement', 16, 'delete_paiement'),
(64, 'Can view paiement', 16, 'view_paiement'),
(65, 'Can add Bordereau', 17, 'add_bordereau'),
(66, 'Can change Bordereau', 17, 'change_bordereau'),
(67, 'Can delete Bordereau', 17, 'delete_bordereau'),
(68, 'Can view Bordereau', 17, 'view_bordereau'),
(69, 'Can add charge', 18, 'add_charge'),
(70, 'Can change charge', 18, 'change_charge'),
(71, 'Can delete charge', 18, 'delete_charge'),
(72, 'Can view charge', 18, 'view_charge'),
(73, 'Can add group chat', 19, 'add_groupchat'),
(74, 'Can change group chat', 19, 'change_groupchat'),
(75, 'Can delete group chat', 19, 'delete_groupchat'),
(76, 'Can view group chat', 19, 'view_groupchat'),
(77, 'Can add group message', 20, 'add_groupmessage'),
(78, 'Can change group message', 20, 'change_groupmessage'),
(79, 'Can delete group message', 20, 'delete_groupmessage'),
(80, 'Can view group message', 20, 'view_groupmessage'),
(81, 'Can add Notification', 21, 'add_notification'),
(82, 'Can change Notification', 21, 'change_notification'),
(83, 'Can delete Notification', 21, 'delete_notification'),
(84, 'Can view Notification', 21, 'view_notification'),
(85, 'Can add bordereau virement', 22, 'add_bordereauvirement'),
(86, 'Can change bordereau virement', 22, 'change_bordereauvirement'),
(87, 'Can delete bordereau virement', 22, 'delete_bordereauvirement'),
(88, 'Can view bordereau virement', 22, 'view_bordereauvirement');

-- --------------------------------------------------------

--
-- Table structure for table `charges_charge`
--

CREATE TABLE `charges_charge` (
  `id` bigint(20) NOT NULL,
  `libelle` varchar(200) NOT NULL,
  `type_charge` varchar(30) NOT NULL,
  `montant_ttc` decimal(12,2) NOT NULL,
  `date_charge` date NOT NULL,
  `notes` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `immeuble_id` bigint(20) DEFAULT NULL,
  `local_id` bigint(20) DEFAULT NULL,
  `deleted_at` datetime(6) DEFAULT NULL
) ;

--
-- Dumping data for table `charges_charge`
--

INSERT INTO `charges_charge` (`id`, `libelle`, `type_charge`, `montant_ttc`, `date_charge`, `notes`, `created_at`, `immeuble_id`, `local_id`, `deleted_at`) VALUES
(1, 'traveaux entretien', 'travaux', 450000.00, '2026-05-10', '', '2026-05-10 14:17:35.704000', 1, NULL, NULL),
(2, 'L00099', 'impot_foncier', 6000000.00, '2026-05-14', '', '2026-05-14 14:15:30.956000', 2, NULL, NULL),
(3, 'L00099', 'impot_foncier', 6000000.00, '2026-05-14', '', '2026-05-14 14:15:33.282000', 2, NULL, NULL),
(4, 'L00099', 'impot_foncier', 6000000.00, '2026-05-14', '', '2026-05-14 14:15:33.722000', 2, NULL, NULL),
(5, 'L00099', 'impot_foncier', 6000000.00, '2026-05-14', '', '2026-05-14 14:15:34.346000', 2, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `chat_groupchat`
--

CREATE TABLE `chat_groupchat` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `immeuble_id` bigint(20) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `chat_groupchat`
--

INSERT INTO `chat_groupchat` (`id`, `nom`, `created_at`, `immeuble_id`, `proprietaire_id`) VALUES
(1, 'Chat — Immeuble Rohero Center', '2026-05-09 19:06:28.519000', 1, 1),
(2, 'Chat — Immeuble', '2026-05-26 12:07:07.214000', 2, 1),
(4, 'Chat — Ndamama House', '2026-06-03 10:24:51.617000', 5, 4),
(5, 'Chat — Ndongozi', '2026-06-08 07:18:17.025000', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `chat_groupmessage`
--

CREATE TABLE `chat_groupmessage` (
  `id` bigint(20) NOT NULL,
  `contenu` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `auteur_id` bigint(20) DEFAULT NULL,
  `group_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `chat_groupmessage`
--

INSERT INTO `chat_groupmessage` (`id`, `contenu`, `created_at`, `auteur_id`, `group_id`) VALUES
(1, 'hhhhh', '2026-05-26 11:59:55.044000', 4, 1),
(2, 'Bonjour', '2026-05-26 12:00:40.454000', 2, 1),
(3, 'Hello', '2026-05-26 12:07:37.248000', 2, 2),
(5, 'hh', '2026-05-28 08:51:44.876000', 4, 1),
(6, '^Saluuuuut', '2026-05-29 12:31:49.988000', 4, 1),
(7, 'saluuuuuuuuuuuuuu', '2026-05-30 06:42:56.349000', 11, 1),
(9, 'helooooooooooooo', '2026-05-30 19:20:08.726000', 4, 1),
(11, 'hi', '2026-06-03 10:25:00.486000', 1, 4),
(12, 'sqlu', '2026-06-04 11:32:24.013000', 3, 1),
(13, 'hello', '2026-06-04 12:09:21.658000', 4, 1),
(14, 'hi', '2026-06-09 09:43:49.901000', 2, 4);

-- --------------------------------------------------------

--
-- Table structure for table `contrats_bordereauvirement`
--

CREATE TABLE `contrats_bordereauvirement` (
  `id` bigint(20) NOT NULL,
  `montant` decimal(12,2) NOT NULL,
  `date_virement` date NOT NULL,
  `reference_virement` varchar(100) DEFAULT NULL,
  `banque` varchar(100) DEFAULT NULL,
  `fichier` varchar(500) NOT NULL,
  `statut` varchar(20) NOT NULL,
  `commentaire_admin` longtext DEFAULT NULL,
  `date_traitement` datetime(6) DEFAULT NULL,
  `date_creation` datetime(6) NOT NULL,
  `contrat_societe_id` bigint(20) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL,
  `traite_par_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `contrats_bordereauvirement`
--

INSERT INTO `contrats_bordereauvirement` (`id`, `montant`, `date_virement`, `reference_virement`, `banque`, `fichier`, `statut`, `commentaire_admin`, `date_traitement`, `date_creation`, `contrat_societe_id`, `proprietaire_id`, `traite_par_id`) VALUES
(1, 450000.00, '2026-07-07', '45875555', '', '03f4ed22-2afe-4d44-acc0-bd9f5b1df92b', 'valide', NULL, '2026-07-07 09:37:01.711000', '2026-07-07 09:26:04.485000', 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `contrats_contrat`
--

CREATE TABLE `contrats_contrat` (
  `id` bigint(20) NOT NULL,
  `numero` varchar(50) NOT NULL,
  `statut` varchar(20) NOT NULL DEFAULT 'actif',
  `loyer_hors_charges` decimal(12,2) NOT NULL,
  `provisions_charges` decimal(12,2) NOT NULL DEFAULT 0.00,
  `periodicite` varchar(20) NOT NULL DEFAULT 'mensuel',
  `depot_garantie` decimal(12,2) NOT NULL DEFAULT 0.00,
  `date_entree` date NOT NULL,
  `date_sortie` date DEFAULT NULL,
  `informations_complementaires` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `local_id` bigint(20) NOT NULL,
  `locataire_id` bigint(20) NOT NULL,
  `local_actif_uniq` bigint(20) GENERATED ALWAYS AS (case when `statut` = 'actif' then `local_id` else NULL end) STORED,
  `deleted_at` datetime(6) DEFAULT NULL
) ;

--
-- Dumping data for table `contrats_contrat`
--

INSERT INTO `contrats_contrat` (`id`, `numero`, `statut`, `loyer_hors_charges`, `provisions_charges`, `periodicite`, `depot_garantie`, `date_entree`, `date_sortie`, `informations_complementaires`, `created_at`, `local_id`, `locataire_id`, `deleted_at`) VALUES
(1, 'C-2026-001', 'actif', 300000.00, 25000.00, 'mensuel', 600000.00, '2026-01-01', NULL, '', '2026-05-09 19:06:29.890000', 1, 1, NULL),
(2, 'c-2026-002', 'resilie', 350000.00, 0.00, 'mensuel', 0.00, '2026-05-10', NULL, '', '2026-05-10 19:02:44.857000', 1, 2, NULL),
(3, 'C-2026-05-12', 'actif', 400000.00, 0.00, 'mensuel', 0.00, '2026-05-12', NULL, '', '2026-05-12 15:33:11.093000', 3, 3, NULL),
(4, 'C-Ndamma-2026', 'actif', 300000.00, 0.00, 'mensuel', 0.00, '2026-06-03', NULL, '', '2026-06-03 10:24:31.033000', 5, 4, NULL),
(5, 'c-5-2026', 'expire', 300000.00, 0.00, 'mensuel', 0.00, '2026-06-04', '2027-06-04', '', '2026-06-04 11:37:33.159000', 5, 5, NULL),
(6, '07-24-2026-c-002', 'actif', 600000.00, 0.00, 'mensuel', 1200000.00, '2026-07-24', '2027-07-24', '', '2026-07-24 09:26:44.743484', 7, 6, NULL);

--
-- Triggers `contrats_contrat`
--
DELIMITER $$
CREATE TRIGGER `trg_contrat_propagate_after_update` AFTER UPDATE ON `contrats_contrat` FOR EACH ROW BEGIN
  IF NEW.local_id <> OLD.local_id OR NEW.locataire_id <> OLD.locataire_id THEN
    UPDATE loyers_loyer
    SET local_id = NEW.local_id,
        locataire_id = NEW.locataire_id
    WHERE contrat_id = NEW.id;
  END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `contrats_contratsociete`
--

CREATE TABLE `contrats_contratsociete` (
  `id` bigint(20) NOT NULL,
  `numero` varchar(50) NOT NULL,
  `date_signature` date NOT NULL,
  `date_effet` date NOT NULL,
  `date_expiration` date DEFAULT NULL,
  `statut` varchar(20) NOT NULL,
  `taux_commission` decimal(5,2) NOT NULL,
  `periodicite_reversement` varchar(20) NOT NULL,
  `frais_entree` decimal(12,2) NOT NULL,
  `service_gestion_loyers` tinyint(1) NOT NULL,
  `service_quittances` tinyint(1) NOT NULL,
  `service_recherche_locataires` tinyint(1) NOT NULL,
  `service_gestion_travaux` tinyint(1) NOT NULL,
  `service_suivi_fiscal` tinyint(1) NOT NULL,
  `service_rapports` tinyint(1) NOT NULL,
  `service_loyers_impayes` tinyint(1) NOT NULL,
  `service_assurances` tinyint(1) NOT NULL,
  `service_judiciaire` tinyint(1) NOT NULL,
  `service_impots_locatifs` tinyint(1) NOT NULL,
  `service_clients` tinyint(1) NOT NULL,
  `service_touristique` tinyint(1) NOT NULL,
  `clauses_particulieres` longtext NOT NULL,
  `notes_internes` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL,
  `constat_lieu` tinyint(1) NOT NULL,
  `inventaire_immeuble` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `contrats_contratsociete`
--

INSERT INTO `contrats_contratsociete` (`id`, `numero`, `date_signature`, `date_effet`, `date_expiration`, `statut`, `taux_commission`, `periodicite_reversement`, `frais_entree`, `service_gestion_loyers`, `service_quittances`, `service_recherche_locataires`, `service_gestion_travaux`, `service_suivi_fiscal`, `service_rapports`, `service_loyers_impayes`, `service_assurances`, `service_judiciaire`, `service_impots_locatifs`, `service_clients`, `service_touristique`, `clauses_particulieres`, `notes_internes`, `created_at`, `proprietaire_id`, `constat_lieu`, `inventaire_immeuble`) VALUES
(1, 'CS-2026-662', '2026-05-10', '2026-05-10', '2027-05-10', 'actif', 10.00, 'mensuel', 4000000.00, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, '', '', '2026-05-10 14:18:45.631000', 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'auth', 'permission'),
(2, 'auth', 'group'),
(3, 'contenttypes', 'contenttype'),
(4, 'auth_app', 'user'),
(5, 'proprietaires', 'proprietaire'),
(6, 'locataires', 'locataire'),
(7, 'admin', 'logentry'),
(8, 'sessions', 'session'),
(9, 'authtoken', 'token'),
(10, 'authtoken', 'tokenproxy'),
(11, 'immeubles', 'immeuble'),
(12, 'locaux', 'local'),
(13, 'contrats', 'contratsociete'),
(14, 'contrats', 'contrat'),
(15, 'loyers', 'loyer'),
(16, 'loyers', 'paiement'),
(17, 'loyers', 'bordereau'),
(18, 'charges', 'charge'),
(19, 'chat', 'groupchat'),
(20, 'chat', 'groupmessage'),
(21, 'notifications', 'notification'),
(22, 'contrats', 'bordereauvirement');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-05-09 19:04:53.008505'),
(2, 'proprietaires', '0001_initial', '2026-05-09 19:04:53.248321'),
(3, 'locataires', '0001_initial', '2026-05-09 19:04:53.417358'),
(4, 'contenttypes', '0002_remove_content_type_name', '2026-05-09 19:04:54.121556'),
(5, 'auth', '0001_initial', '2026-05-09 19:04:57.093874'),
(6, 'auth', '0002_alter_permission_name_max_length', '2026-05-09 19:04:57.657807'),
(7, 'auth', '0003_alter_user_email_max_length', '2026-05-09 19:04:57.736016'),
(8, 'auth', '0004_alter_user_username_opts', '2026-05-09 19:04:57.768470'),
(9, 'auth', '0005_alter_user_last_login_null', '2026-05-09 19:04:57.790737'),
(10, 'auth', '0006_require_contenttypes_0002', '2026-05-09 19:04:57.803644'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2026-05-09 19:04:57.825124'),
(12, 'auth', '0008_alter_user_username_max_length', '2026-05-09 19:04:57.843452'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2026-05-09 19:04:57.866821'),
(14, 'auth', '0010_alter_group_name_max_length', '2026-05-09 19:04:58.230842'),
(15, 'auth', '0011_update_proxy_permissions', '2026-05-09 19:04:58.289415'),
(16, 'auth', '0012_alter_user_first_name_max_length', '2026-05-09 19:04:58.331986'),
(17, 'auth_app', '0001_initial', '2026-05-09 19:05:03.731710'),
(18, 'admin', '0001_initial', '2026-05-09 19:05:35.058327'),
(19, 'admin', '0002_logentry_remove_auto_add', '2026-05-09 19:05:35.115063'),
(20, 'admin', '0003_logentry_add_action_flag_choices', '2026-05-09 19:05:35.159112'),
(21, 'authtoken', '0001_initial', '2026-05-09 19:05:36.032678'),
(22, 'authtoken', '0002_auto_20160226_1747', '2026-05-09 19:05:36.110740'),
(23, 'authtoken', '0003_tokenproxy', '2026-05-09 19:05:36.134940'),
(24, 'immeubles', '0001_initial', '2026-05-09 19:05:36.314464'),
(25, 'locaux', '0001_initial', '2026-05-09 19:05:37.843218'),
(26, 'charges', '0001_initial', '2026-05-09 19:05:38.978709'),
(27, 'chat', '0001_initial', '2026-05-09 19:05:41.314716'),
(28, 'contrats', '0001_initial', '2026-05-09 19:05:43.943084'),
(29, 'loyers', '0001_initial', '2026-05-09 19:05:48.205756'),
(30, 'notifications', '0001_initial', '2026-05-09 19:05:49.655064'),
(31, 'sessions', '0001_initial', '2026-05-09 19:05:50.218265'),
(32, 'locataires', '0002_locataire_mot_de_passe_temp', '2026-06-01 11:09:11.039441'),
(33, 'proprietaires', '0002_proprietaire_mot_de_passe_temp', '2026-06-01 11:09:11.855706'),
(34, 'immeubles', '0002_immeuble_proprietaire', '2026-06-03 10:10:02.527962'),
(35, 'locataires', '0003_locataire_user', '2026-06-04 14:05:03.872760'),
(36, 'locataires', '0004_remove_locataire_user', '2026-06-05 08:53:47.198671'),
(37, 'contrats', '0002_contratsociete_constat_lieu_and_more', '2026-06-09 08:47:25.285555'),
(38, 'loyers', '0002_alter_bordereau_photo', '2026-06-19 16:22:29.644859'),
(39, 'contrats', '0003_bordereauvirement', '2026-07-07 08:41:30.509437'),
(40, 'notifications', '0002_notification_loyer', '2026-07-09 10:18:25.635922'),
(41, 'loyers', '0003_loyer_quittance_envoyee', '2026-07-09 10:32:15.651168'),
(42, 'immeubles', '0003_alter_immeuble_adresse_province', '2026-07-14 09:52:36.904321'),
(43, 'charges', '0002_charge_deleted_at_and_more', '2026-07-23 11:17:22.032707'),
(44, 'contrats', '0004_contrat_deleted_at_contrat_chk_contrat_statut_and_more', '2026-07-23 12:00:02.318035'),
(45, 'locataires', '0005_locataire_uniq_locataire_email_and_more', '2026-07-23 12:05:13.697683'),
(46, 'loyers', '0004_loyer_deleted_at_alter_loyer_contrat_and_more', '2026-07-23 12:08:03.877395'),
(47, 'proprietaires', '0003_proprietaire_uniq_proprietaire_email_and_more', '2026-07-23 12:11:43.432016');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0y7gf5ive7kpps1a5yjsouiv607pquie', '.eJxVjDsOwjAQBe_iGllefxdK-pzBsr0bHECxFCcV4u4QKQW0b2beS8S0rTVunZc4kbgIEKffLafy4HkHdE_zrcnS5nWZstwVedAuh0b8vB7u30FNvX5rVBi8gsRkKDgKYBjAo3YeRsjGKhswFEeAwN5rPGvLI6ICHDMV5cT7A6vxNow:1wLnC3:s5extTXFQgFHfHmaeUiHdp3E2PyzhL1GZIoXIVFj4Lg', '2026-05-23 19:18:31.184301');

-- --------------------------------------------------------

--
-- Table structure for table `immeubles_immeuble`
--

CREATE TABLE `immeubles_immeuble` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(200) NOT NULL,
  `adresse_province` varchar(100) NOT NULL,
  `adresse_commune` varchar(100) NOT NULL,
  `adresse_quartier` varchar(100) NOT NULL,
  `annee_construction` int(11) DEFAULT NULL,
  `informations_complementaires` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `proprietaire_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `immeubles_immeuble`
--

INSERT INTO `immeubles_immeuble` (`id`, `nom`, `adresse_province`, `adresse_commune`, `adresse_quartier`, `annee_construction`, `informations_complementaires`, `created_at`, `proprietaire_id`) VALUES
(1, 'Immeuble Rohero Center', 'Bujumbura', 'Mukaza', 'Rohero', 2018, '', '2026-05-09 19:06:28.484000', NULL),
(2, 'Immeuble', 'Bujumbura', 'Mukaza', 'Rohero', 2015, '', '2026-05-10 18:58:53.185000', NULL),
(3, 'Ndongozi', 'Bujumbura', 'Mukaza', 'rohero', 2017, '', '2026-05-11 07:08:17.647000', NULL),
(4, 'VMarket', 'Bujumbura', 'Mukaza', 'Rohero', NULL, '', '2026-05-26 15:32:33.923000', NULL),
(5, 'Ndamama House', 'Bujumbura', 'Mukaza', 'Rohero', NULL, '', '2026-06-03 10:21:58.475000', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `locataires_locataire`
--

CREATE TABLE `locataires_locataire` (
  `id` bigint(20) NOT NULL,
  `nom_prenom` varchar(200) NOT NULL,
  `telephone` varchar(30) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `adresse_postale` varchar(300) NOT NULL,
  `informations_complementaires` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `mot_de_passe_temp` varchar(128) NOT NULL,
  `email_uniq` varchar(254) GENERATED ALWAYS AS (case when `email` <> '' then `email` else NULL end) STORED,
  `telephone_uniq` varchar(30) GENERATED ALWAYS AS (case when `telephone` <> '' then `telephone` else NULL end) STORED
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `locataires_locataire`
--

INSERT INTO `locataires_locataire` (`id`, `nom_prenom`, `telephone`, `email`, `adresse_postale`, `informations_complementaires`, `created_at`, `mot_de_passe_temp`) VALUES
(1, 'HABIMANA Patrick', '+257 79 002 002', 'patrick@email.com', '', '', '2026-05-09 19:06:28.694000', ''),
(2, 'Gerard', '', '', '', '', '2026-05-10 19:01:45.108000', ''),
(3, 'Eva Ntibantunganya', '', 'evnet@gmail.com', '', '', '2026-05-12 15:32:07.839000', ''),
(4, 'Nahayo Remy', '25775200221', 'remy@gmail.com', '', '', '2026-06-03 10:23:38.250000', ''),
(5, 'Hilaire Ngenzebuhoro', '', '', '', '', '2026-06-04 11:35:40.517000', ''),
(6, 'Gakware Gerard', '75202125', 'ger@gmail.com', '-', '', '2026-07-24 09:25:19.685992', '');

-- --------------------------------------------------------

--
-- Table structure for table `locaux_local`
--

CREATE TABLE `locaux_local` (
  `id` bigint(20) NOT NULL,
  `reference` varchar(50) NOT NULL,
  `type_local` varchar(20) NOT NULL,
  `adresse_province` varchar(100) NOT NULL,
  `adresse_commune` varchar(100) NOT NULL,
  `adresse_quartier` varchar(100) NOT NULL,
  `superficie` decimal(8,2) DEFAULT NULL,
  `annee_construction` int(11) DEFAULT NULL,
  `meuble` tinyint(1) NOT NULL,
  `informations_complementaires` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `immeuble_id` bigint(20) DEFAULT NULL,
  `proprietaire_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `locaux_local`
--

INSERT INTO `locaux_local` (`id`, `reference`, `type_local`, `adresse_province`, `adresse_commune`, `adresse_quartier`, `superficie`, `annee_construction`, `meuble`, `informations_complementaires`, `created_at`, `immeuble_id`, `proprietaire_id`) VALUES
(1, 'L-001', 'appartement', 'Bujumbura', 'Mukaza', 'Rohero', 65.00, NULL, 1, '', '2026-05-09 19:06:28.672000', 1, 1),
(2, 'L-002', 'appartement', 'Gitega', 'Mutumba', 'Musinzira', 230.00, NULL, 1, '', '2026-05-10 19:00:02.951000', 2, 1),
(3, 'C4410', 'bureau', 'Bujumbura', 'Ntahangwa', 'Kigobe Nord', 9.00, 2018, 1, '', '2026-05-12 15:30:49.420000', 3, 1),
(5, 'Ndamm-L0012', 'maison', 'Bujumbura', 'Mukaza', 'Rohero', 200.00, NULL, 1, '', '2026-06-03 10:22:58.373000', 5, 4),
(7, '0111', 'appartement', '', '', '', 5000.00, 2015, 1, 'kiriri', '2026-07-06 08:34:30.003000', 4, 5),
(8, '01141', 'appartement', '', '', '', 25000.00, 2015, 1, '', '2026-07-06 08:35:53.309000', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `loyers_bordereau`
--

CREATE TABLE `loyers_bordereau` (
  `id` bigint(20) NOT NULL,
  `photo` longtext DEFAULT NULL,
  `notes` longtext NOT NULL,
  `reference_paiement` varchar(50) DEFAULT NULL,
  `statut` varchar(20) NOT NULL,
  `commentaire_admin` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `locataire_id` bigint(20) NOT NULL,
  `loyer_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `loyers_bordereau`
--

INSERT INTO `loyers_bordereau` (`id`, `photo`, `notes`, `reference_paiement`, `statut`, `commentaire_admin`, `created_at`, `locataire_id`, `loyer_id`) VALUES
(1, NULL, '', NULL, 'valide', '', '2026-05-10 07:11:31.171000', 1, NULL),
(13, NULL, '', NULL, 'valide', '', '2026-05-11 08:52:44.931000', 1, NULL),
(24, NULL, '', NULL, 'valide', '', '2026-05-22 14:08:13.075000', 1, NULL),
(25, NULL, '', NULL, 'valide', '', '2026-06-02 14:30:01.578000', 1, NULL),
(26, NULL, '', NULL, 'valide', '', '2026-06-02 14:32:06.060000', 1, 31),
(27, NULL, '2020200', NULL, 'en_attente', '', '2026-06-30 07:22:32.886000', 1, 34),
(28, NULL, '200522', NULL, 'en_attente', '', '2026-06-30 15:53:42.721000', 1, 34),
(29, NULL, '20000001111', NULL, 'en_attente', '', '2026-06-30 17:04:01.946000', 1, 34),
(30, NULL, '502222222', NULL, 'en_attente', '', '2026-07-02 08:14:25.958000', 1, 34),
(31, NULL, '55555555', NULL, 'en_attente', '', '2026-07-02 09:15:00.052000', 1, 34),
(32, NULL, '888888888', NULL, 'en_attente', '', '2026-07-02 09:20:47.066000', 1, 34),
(33, NULL, '77777777777777', NULL, 'en_attente', '', '2026-07-02 10:30:16.638000', 1, 34),
(34, NULL, '6666666666666', NULL, 'en_attente', '', '2026-07-02 11:05:48.354000', 1, 35),
(35, NULL, '22222222222222222', NULL, 'en_attente', '', '2026-07-02 11:20:38.523000', 1, 34),
(36, NULL, '11111111111111111111111111111', NULL, 'valide', '', '2026-07-02 11:33:00.167000', 1, 36);

-- --------------------------------------------------------

--
-- Table structure for table `loyers_loyer`
--

CREATE TABLE `loyers_loyer` (
  `id` bigint(20) NOT NULL,
  `libelle` varchar(200) NOT NULL,
  `periode_debut` date NOT NULL,
  `periode_fin` date DEFAULT NULL,
  `loyer_hors_charges` decimal(12,2) NOT NULL,
  `charges` decimal(12,2) NOT NULL,
  `echeance` date NOT NULL,
  `statut` varchar(20) NOT NULL,
  `informations_complementaires` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `contrat_id` bigint(20) NOT NULL,
  `local_id` bigint(20) NOT NULL,
  `locataire_id` bigint(20) NOT NULL,
  `quittance_envoyee` tinyint(1) NOT NULL,
  `deleted_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `loyers_loyer`
--

INSERT INTO `loyers_loyer` (`id`, `libelle`, `periode_debut`, `periode_fin`, `loyer_hors_charges`, `charges`, `echeance`, `statut`, `informations_complementaires`, `created_at`, `contrat_id`, `local_id`, `locataire_id`, `quittance_envoyee`, `deleted_at`) VALUES
(30, 'Loyer 2026', '2026-06-02', NULL, 300000.00, 0.00, '2026-06-02', 'paye', '', '2026-06-02 12:40:59.181000', 3, 3, 1, 0, NULL),
(31, 'Loyer June 2026', '2026-06-02', '2026-07-01', 300000.00, 25000.00, '2026-06-02', 'paye', '', '2026-06-02 14:30:49.142000', 1, 1, 1, 0, NULL),
(32, 'Loyer July 2026', '2026-07-02', '2026-08-01', 300000.00, 25000.00, '2026-07-02', 'paye', '', '2026-06-02 14:30:49.231000', 1, 1, 1, 0, NULL),
(33, 'Loyer August 2026', '2026-08-02', '2026-09-01', 300000.00, 25000.00, '2026-08-02', 'paye', '', '2026-06-02 14:30:49.402000', 1, 1, 1, 0, NULL),
(34, 'Loyer September 2026', '2026-09-02', '2026-10-01', 300000.00, 25000.00, '2026-09-02', 'paye', '', '2026-06-02 14:30:49.500000', 1, 1, 1, 0, NULL),
(35, 'Loyer October 2026', '2026-10-02', '2026-11-01', 300000.00, 25000.00, '2026-10-02', 'paye', '', '2026-06-02 14:30:49.572000', 1, 1, 1, 0, NULL),
(36, 'Loyer November 2026', '2026-11-02', '2026-12-01', 300000.00, 25000.00, '2026-11-02', 'attente', '', '2026-06-02 14:30:49.623000', 1, 1, 1, 0, NULL),
(37, 'Loyer December 2026', '2026-12-02', '2027-01-01', 300000.00, 25000.00, '2026-12-02', 'paye', '', '2026-06-02 14:30:49.671000', 1, 1, 1, 0, NULL),
(38, 'Loyer January 2027', '2027-01-02', '2027-02-01', 300000.00, 25000.00, '2027-01-02', 'paye', '', '2026-06-02 14:30:49.729000', 1, 1, 1, 0, NULL),
(39, 'Loyer February 2027', '2027-02-02', '2027-03-01', 300000.00, 25000.00, '2027-02-02', 'paye', '', '2026-06-02 14:30:49.777000', 1, 1, 1, 0, NULL),
(40, 'Loyer March 2027', '2027-03-02', '2027-04-01', 300000.00, 25000.00, '2027-03-02', 'paye', '', '2026-06-02 14:30:49.843000', 1, 1, 1, 0, NULL),
(41, 'Loyer April 2027', '2027-04-02', '2027-05-01', 300000.00, 25000.00, '2027-04-02', 'paye', '', '2026-06-02 14:30:49.910000', 1, 1, 1, 0, NULL),
(42, 'Loyer May 2027', '2027-05-02', '2027-06-01', 300000.00, 25000.00, '2027-05-02', 'paye', '', '2026-06-02 14:30:49.987000', 1, 1, 1, 0, NULL),
(43, 'Loyer June 2026', '2026-06-03', '2026-07-02', 300000.00, 0.00, '2026-06-03', 'attente', '', '2026-06-03 14:39:53.669000', 4, 5, 4, 0, NULL),
(44, 'Loyer July 2026', '2026-07-03', '2026-08-02', 300000.00, 0.00, '2026-07-03', 'attente', '', '2026-06-03 14:39:53.753000', 4, 5, 4, 0, NULL),
(45, 'Loyer August 2026', '2026-08-03', '2026-09-02', 300000.00, 0.00, '2026-08-03', 'attente', '', '2026-06-03 14:39:53.835000', 4, 5, 4, 0, NULL),
(46, 'Loyer September 2026', '2026-09-03', '2026-10-02', 300000.00, 0.00, '2026-09-03', 'attente', '', '2026-06-03 14:39:53.877000', 4, 5, 4, 0, NULL),
(47, 'Loyer October 2026', '2026-10-03', '2026-11-02', 300000.00, 0.00, '2026-10-03', 'attente', '', '2026-06-03 14:39:53.905000', 4, 5, 4, 0, NULL),
(48, 'Loyer November 2026', '2026-11-03', '2026-12-02', 300000.00, 0.00, '2026-11-03', 'paye', '', '2026-06-03 14:39:53.937000', 4, 5, 4, 0, NULL),
(49, 'Loyer December 2026', '2026-12-03', '2027-01-02', 300000.00, 0.00, '2026-12-03', 'paye', '', '2026-06-03 14:39:54.009000', 4, 5, 4, 0, NULL),
(50, 'Loyer January 2027', '2027-01-03', '2027-02-02', 300000.00, 0.00, '2027-01-03', 'paye', '', '2026-06-03 14:39:54.048000', 4, 5, 4, 0, NULL),
(51, 'Loyer February 2027', '2027-02-03', '2027-03-02', 300000.00, 0.00, '2027-02-03', 'paye', '', '2026-06-03 14:39:54.059000', 4, 5, 4, 0, NULL),
(52, 'Loyer March 2027', '2027-03-03', '2027-04-02', 300000.00, 0.00, '2027-03-03', 'paye', '', '2026-06-03 14:39:54.070000', 4, 5, 4, 0, NULL),
(53, 'Loyer April 2027', '2027-04-03', '2027-05-02', 300000.00, 0.00, '2027-04-03', 'paye', '', '2026-06-03 14:39:54.082000', 4, 5, 4, 0, NULL),
(54, 'Loyer May 2027', '2027-05-03', '2027-06-02', 300000.00, 0.00, '2027-05-03', 'paye', '', '2026-06-03 14:39:54.092000', 4, 5, 4, 0, NULL),
(55, 'Loyer June 2026', '2026-06-05', '2026-07-04', 350000.00, 0.00, '2026-06-05', 'attente', '', '2026-06-05 12:10:27.715000', 2, 1, 2, 0, NULL),
(56, 'Loyer July 2026', '2026-07-05', '2026-08-04', 350000.00, 0.00, '2026-07-05', 'attente', '', '2026-06-05 12:10:27.801000', 2, 1, 2, 0, NULL),
(57, 'Loyer August 2026', '2026-08-05', '2026-09-04', 350000.00, 0.00, '2026-08-05', 'attente', '', '2026-06-05 12:10:27.817000', 2, 1, 2, 0, NULL),
(58, 'Loyer September 2026', '2026-09-05', '2026-10-04', 350000.00, 0.00, '2026-09-05', 'paye', '', '2026-06-05 12:10:27.827000', 2, 1, 2, 0, NULL),
(59, 'Loyer June 2026', '2026-06-08', '2026-07-07', 300000.00, 0.00, '2026-06-08', 'attente', '', '2026-06-08 09:52:28.445000', 5, 5, 5, 0, NULL),
(60, 'Loyer July 2026', '2026-07-08', '2026-08-07', 300000.00, 0.00, '2026-07-08', 'attente', '', '2026-06-08 09:52:28.497000', 5, 5, 5, 0, NULL),
(61, 'Loyer August 2026', '2026-08-08', '2026-09-07', 300000.00, 0.00, '2026-08-08', 'attente', '', '2026-06-08 09:52:28.513000', 5, 5, 5, 0, NULL),
(62, 'Loyer September 2026', '2026-09-08', '2026-10-07', 300000.00, 0.00, '2026-09-08', 'attente', '', '2026-06-08 09:52:28.606000', 5, 5, 5, 0, NULL),
(63, 'Loyer October 2026', '2026-10-08', '2026-11-07', 300000.00, 0.00, '2026-10-08', 'attente', '', '2026-06-08 09:52:28.650000', 5, 5, 5, 0, NULL),
(64, 'Loyer November 2026', '2026-11-08', '2026-12-07', 300000.00, 0.00, '2026-11-08', 'paye', '', '2026-06-08 09:52:28.780000', 5, 5, 5, 0, NULL),
(65, 'Loyer December 2026', '2026-12-08', '2027-01-07', 300000.00, 0.00, '2026-12-08', 'paye', '', '2026-06-08 09:52:28.813000', 5, 5, 5, 0, NULL),
(66, 'Loyer January 2027', '2027-01-08', '2027-02-07', 300000.00, 0.00, '2027-01-08', 'paye', '', '2026-06-08 09:52:28.852000', 5, 5, 5, 0, NULL),
(67, 'Loyer February 2027', '2027-02-08', '2027-03-07', 300000.00, 0.00, '2027-02-08', 'paye', '', '2026-06-08 09:52:28.879000', 5, 5, 5, 0, NULL),
(68, 'Loyer March 2027', '2027-03-08', '2027-04-07', 300000.00, 0.00, '2027-03-08', 'paye', '', '2026-06-08 09:52:28.901000', 5, 5, 5, 0, NULL),
(69, 'Loyer April 2027', '2027-04-08', '2027-05-07', 300000.00, 0.00, '2027-04-08', 'paye', '', '2026-06-08 09:52:28.956000', 5, 5, 5, 0, NULL),
(70, 'Loyer May 2027', '2027-05-08', '2027-06-07', 300000.00, 0.00, '2027-05-08', 'paye', '', '2026-06-08 09:52:28.978000', 5, 5, 5, 0, NULL);

--
-- Triggers `loyers_loyer`
--
DELIMITER $$
CREATE TRIGGER `trg_loyer_sync_before_insert` BEFORE INSERT ON `loyers_loyer` FOR EACH ROW BEGIN
  SET NEW.local_id = (SELECT local_id FROM contrats_contrat WHERE id = NEW.contrat_id);
  SET NEW.locataire_id = (SELECT locataire_id FROM contrats_contrat WHERE id = NEW.contrat_id);
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trg_loyer_sync_before_update` BEFORE UPDATE ON `loyers_loyer` FOR EACH ROW BEGIN
  IF NEW.contrat_id <> OLD.contrat_id THEN
    SET NEW.local_id = (SELECT local_id FROM contrats_contrat WHERE id = NEW.contrat_id);
    SET NEW.locataire_id = (SELECT locataire_id FROM contrats_contrat WHERE id = NEW.contrat_id);
  END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `loyers_paiement`
--

CREATE TABLE `loyers_paiement` (
  `id` bigint(20) NOT NULL,
  `montant` decimal(12,2) NOT NULL,
  `date_paiement` date NOT NULL,
  `mode_paiement` varchar(20) NOT NULL,
  `reference` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint(20) DEFAULT NULL,
  `loyer_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `loyers_paiement`
--

INSERT INTO `loyers_paiement` (`id`, `montant`, `date_paiement`, `mode_paiement`, `reference`, `created_at`, `created_by_id`, `loyer_id`) VALUES
(88, 300000.00, '2026-06-02', 'virement', '', '2026-06-02 12:41:09.835000', 1, 30),
(89, 325000.00, '2026-06-02', 'virement', '', '2026-06-02 14:33:07.833000', 2, 31),
(90, 325000.00, '2026-06-03', 'virement', '', '2026-06-03 10:29:08.678000', 1, 32),
(91, 325000.00, '2026-06-03', 'virement', '', '2026-06-03 15:19:14.225000', 1, 33),
(92, 300000.00, '2026-06-03', 'virement', '', '2026-06-03 15:22:51.877000', 1, 39),
(93, 325000.00, '2026-06-05', 'virement', '', '2026-06-05 15:55:18.299000', 1, 39),
(94, 200000.00, '2026-06-08', 'virement', '', '2026-06-08 10:54:45.585000', 2, 70),
(95, 300000.00, '2026-06-09', 'especes', '', '2026-06-09 09:28:51.173000', 1, 70),
(96, 325000.00, '2026-07-06', 'virement', '', '2026-07-06 12:03:43.750000', 1, 34),
(97, 325000.00, '2026-07-06', 'virement', '', '2026-07-06 12:03:58.406000', 1, 35),
(98, 325000.00, '2026-07-06', 'virement', '', '2026-07-06 12:04:03.258000', 1, 42),
(99, 325000.00, '2026-07-06', 'virement', '', '2026-07-06 12:04:07.482000', 1, 41),
(100, 325000.00, '2026-07-06', 'virement', '', '2026-07-06 12:04:11.190000', 1, 40),
(101, 325000.00, '2026-07-06', 'virement', '', '2026-07-06 12:04:16.671000', 1, 38),
(102, 350000.00, '2026-07-06', 'virement', '', '2026-07-06 12:04:24.532000', 1, 58),
(103, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:22:45.585164', 2, 54),
(104, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:22:49.781143', 2, 69),
(105, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:22:53.366365', 2, 53),
(106, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:22:57.792820', 2, 68),
(107, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:01.777320', 2, 52),
(108, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:08.544306', 2, 67),
(109, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:13.462637', 2, 51),
(110, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:17.687279', 2, 66),
(111, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:22.098067', 2, 50),
(112, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:26.568586', 2, 65),
(113, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:30.910240', 2, 49),
(114, 325000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:35.430351', 2, 37),
(115, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:39.846014', 2, 64),
(116, 300000.00, '2026-07-23', 'virement', '', '2026-07-23 12:23:46.178384', 2, 48);

-- --------------------------------------------------------

--
-- Table structure for table `notifications_notification`
--

CREATE TABLE `notifications_notification` (
  `id` bigint(20) NOT NULL,
  `titre` varchar(200) NOT NULL,
  `message` longtext NOT NULL,
  `type_notif` varchar(20) NOT NULL,
  `lu` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `destinataire_locataire_id` bigint(20) DEFAULT NULL,
  `destinataire_proprietaire_id` bigint(20) DEFAULT NULL,
  `loyer_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `notifications_notification`
--

INSERT INTO `notifications_notification` (`id`, `titre`, `message`, `type_notif`, `lu`, `created_at`, `destinataire_locataire_id`, `destinataire_proprietaire_id`, `loyer_id`) VALUES
(1, 'Bordereau validé', 'Votre bordereau de paiement a été validé ✅.', 'bordereau', 1, '2026-05-10 14:10:21.033000', 1, NULL, NULL),
(22, 'Bordereau validé', 'Votre bordereau de paiement a été validé ✅.', 'bordereau', 1, '2026-05-11 08:54:57.914000', 1, NULL, NULL),
(23, 'Bordereau validé', 'Votre bordereau de paiement a été validé ✅.', 'bordereau', 1, '2026-05-26 08:08:32.273000', 1, NULL, NULL),
(24, 'Affirmation paiement', 'Bien recu', 'avertissement', 0, '2026-07-06 08:50:22.080000', 5, NULL, NULL),
(25, 'affirmation paiement', 'bien recu', 'avertissement', 1, '2026-07-06 09:02:58.357000', 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `proprietaires_proprietaire`
--

CREATE TABLE `proprietaires_proprietaire` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(200) NOT NULL,
  `telephone` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `adresse_province` varchar(100) NOT NULL,
  `adresse_commune` varchar(100) NOT NULL,
  `adresse_quartier` varchar(100) NOT NULL,
  `informations_complementaires` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `mot_de_passe_temp` varchar(128) NOT NULL,
  `email_uniq` varchar(254) GENERATED ALWAYS AS (case when `email` <> '' then `email` else NULL end) STORED,
  `telephone_uniq` varchar(30) GENERATED ALWAYS AS (case when `telephone` <> '' then `telephone` else NULL end) STORED
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `proprietaires_proprietaire`
--

INSERT INTO `proprietaires_proprietaire` (`id`, `nom`, `telephone`, `email`, `adresse_province`, `adresse_commune`, `adresse_quartier`, `informations_complementaires`, `created_at`, `mot_de_passe_temp`) VALUES
(1, 'NKURUNZIZA Jean Pierre', '+257 79 001 001', 'jean@email.com', 'Bujumbura', 'Mukaza', 'Rohero', '', '2026-05-09 19:06:27.534000', ''),
(2, 'Ruberinyange Johnatta', '2576800232', 'johnatta@gmail.com', 'Bujumbura', 'Mukaza', 'Rohero', '', '2026-05-12 15:28:06.126000', ''),
(4, 'Ngenzebuhoro Hilaire', '2573022255', 'hilaire@gmail.com', 'Bujumbura', 'Mukaza', 'Rohero', '', '2026-06-03 10:21:24.198000', ''),
(5, 'Gahungu Eloi', '', '', 'Gitega', 'Gitega', '', '', '2026-06-05 10:38:57.255000', ''),
(6, 'Karenzo Jean', '66232120', 'jean@gmail.com', 'Buhumuza', 'Butaganzwa', '', '', '2026-07-24 09:19:44.817732', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `authtoken_token_user_id_uniq` (`user_id`);

--
-- Indexes for table `auth_app_user`
--
ALTER TABLE `auth_app_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_app_user_username_uniq` (`username`),
  ADD UNIQUE KEY `auth_app_user_locataire_profile_uniq` (`locataire_profile_id`),
  ADD UNIQUE KEY `auth_app_user_proprietaire_profile_uniq` (`proprietaire_profile_id`);

--
-- Indexes for table `auth_app_user_groups`
--
ALTER TABLE `auth_app_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_app_user_groups_user_id_group_id_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_app_user_groups_group_id_b4576925_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_app_user_user_permissions`
--
ALTER TABLE `auth_app_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_app_user_user_permissions_user_id_permission_id_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_app_user_user_p_permission_id_cc1b2396_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD KEY `auth_permission_content_type_id_2f476e4b_fk_django_co` (`content_type_id`);

--
-- Indexes for table `charges_charge`
--
ALTER TABLE `charges_charge`
  ADD PRIMARY KEY (`id`),
  ADD KEY `charges_charge_immeuble_id_idx` (`immeuble_id`),
  ADD KEY `charges_charge_local_id_idx` (`local_id`);

--
-- Indexes for table `chat_groupchat`
--
ALTER TABLE `chat_groupchat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `chat_groupchat_immeuble_id_e831694e_fk_immeubles_immeuble_id` (`immeuble_id`),
  ADD KEY `chat_groupchat_proprietaire_id_2d7dba35_fk_proprieta` (`proprietaire_id`);

--
-- Indexes for table `chat_groupmessage`
--
ALTER TABLE `chat_groupmessage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `chat_groupmessage_auteur_id_6c435380_fk_auth_app_user_id` (`auteur_id`),
  ADD KEY `chat_groupmessage_group_id_754429fc_fk_chat_groupchat_id` (`group_id`);

--
-- Indexes for table `contrats_bordereauvirement`
--
ALTER TABLE `contrats_bordereauvirement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `contrats_bordereauvi_contrat_societe_id_2f3d7d17_fk_contrats_` (`contrat_societe_id`),
  ADD KEY `contrats_bordereauvi_proprietaire_id_c2578159_fk_proprieta` (`proprietaire_id`),
  ADD KEY `contrats_bordereauvi_traite_par_id_3d0c6167_fk_auth_app_` (`traite_par_id`);

--
-- Indexes for table `contrats_contrat`
--
ALTER TABLE `contrats_contrat`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `contrats_contrat_numero_uniq` (`numero`),
  ADD UNIQUE KEY `uniq_local_actif` (`local_actif_uniq`),
  ADD KEY `contrats_contrat_local_id_idx` (`local_id`),
  ADD KEY `contrats_contrat_locataire_id_idx` (`locataire_id`);

--
-- Indexes for table `contrats_contratsociete`
--
ALTER TABLE `contrats_contratsociete`
  ADD PRIMARY KEY (`id`),
  ADD KEY `contrats_contratsoci_proprietaire_id_3dbb5fc2_fk_proprieta` (`proprietaire_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_app_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`);

--
-- Indexes for table `immeubles_immeuble`
--
ALTER TABLE `immeubles_immeuble`
  ADD PRIMARY KEY (`id`),
  ADD KEY `immeubles_immeuble_proprietaire_id_f3a805ad_fk_proprieta` (`proprietaire_id`);

--
-- Indexes for table `locataires_locataire`
--
ALTER TABLE `locataires_locataire`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uniq_locataire_email` (`email_uniq`),
  ADD UNIQUE KEY `uniq_locataire_telephone` (`telephone_uniq`);

--
-- Indexes for table `locaux_local`
--
ALTER TABLE `locaux_local`
  ADD PRIMARY KEY (`id`),
  ADD KEY `locaux_local_immeuble_id_d7d3aa78_fk_immeubles_immeuble_id` (`immeuble_id`),
  ADD KEY `locaux_local_proprietaire_id_fe20c28d_fk_proprieta` (`proprietaire_id`);

--
-- Indexes for table `loyers_bordereau`
--
ALTER TABLE `loyers_bordereau`
  ADD PRIMARY KEY (`id`),
  ADD KEY `loyers_bordereau_locataire_id_idx` (`locataire_id`),
  ADD KEY `loyers_bordereau_loyer_id_idx` (`loyer_id`);

--
-- Indexes for table `loyers_loyer`
--
ALTER TABLE `loyers_loyer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `loyers_loyer_contrat_id_idx` (`contrat_id`),
  ADD KEY `loyers_loyer_local_id_idx` (`local_id`),
  ADD KEY `loyers_loyer_locataire_id_idx` (`locataire_id`);

--
-- Indexes for table `loyers_paiement`
--
ALTER TABLE `loyers_paiement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `loyers_paiement_created_by_id_5fcdb5fc_fk_auth_app_user_id` (`created_by_id`),
  ADD KEY `loyers_paiement_loyer_id_60c19813_fk_loyers_loyer_id` (`loyer_id`);

--
-- Indexes for table `notifications_notification`
--
ALTER TABLE `notifications_notification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notifications_notifi_destinataire_locatai_fce6358c_fk_locataire` (`destinataire_locataire_id`),
  ADD KEY `notifications_notifi_destinataire_proprie_ae10a113_fk_proprieta` (`destinataire_proprietaire_id`),
  ADD KEY `notifications_notification_loyer_id_c6e28362_fk_loyers_loyer_id` (`loyer_id`);

--
-- Indexes for table `proprietaires_proprietaire`
--
ALTER TABLE `proprietaires_proprietaire`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uniq_proprietaire_email` (`email_uniq`),
  ADD UNIQUE KEY `uniq_proprietaire_telephone` (`telephone_uniq`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_app_user`
--
ALTER TABLE `auth_app_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_app_user_groups`
--
ALTER TABLE `auth_app_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_app_user_user_permissions`
--
ALTER TABLE `auth_app_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `charges_charge`
--
ALTER TABLE `charges_charge`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chat_groupchat`
--
ALTER TABLE `chat_groupchat`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `chat_groupmessage`
--
ALTER TABLE `chat_groupmessage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `contrats_bordereauvirement`
--
ALTER TABLE `contrats_bordereauvirement`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `contrats_contrat`
--
ALTER TABLE `contrats_contrat`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `contrats_contratsociete`
--
ALTER TABLE `contrats_contratsociete`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `immeubles_immeuble`
--
ALTER TABLE `immeubles_immeuble`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `locataires_locataire`
--
ALTER TABLE `locataires_locataire`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `locaux_local`
--
ALTER TABLE `locaux_local`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `loyers_bordereau`
--
ALTER TABLE `loyers_bordereau`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `loyers_loyer`
--
ALTER TABLE `loyers_loyer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT for table `loyers_paiement`
--
ALTER TABLE `loyers_paiement`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=117;

--
-- AUTO_INCREMENT for table `notifications_notification`
--
ALTER TABLE `notifications_notification`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `proprietaires_proprietaire`
--
ALTER TABLE `proprietaires_proprietaire`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_app_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_app_user` (`id`);

--
-- Constraints for table `auth_app_user`
--
ALTER TABLE `auth_app_user`
  ADD CONSTRAINT `auth_app_user_locataire_profile_id_6bbe96aa_fk_locataire` FOREIGN KEY (`locataire_profile_id`) REFERENCES `locataires_locataire` (`id`),
  ADD CONSTRAINT `auth_app_user_proprietaire_profile_01b059e1_fk_proprieta` FOREIGN KEY (`proprietaire_profile_id`) REFERENCES `proprietaires_proprietaire` (`id`);

--
-- Constraints for table `auth_app_user_groups`
--
ALTER TABLE `auth_app_user_groups`
  ADD CONSTRAINT `auth_app_user_groups_group_id_b4576925_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_app_user_groups_user_id_2b6e45f5_fk_auth_app_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_app_user` (`id`);

--
-- Constraints for table `auth_app_user_user_permissions`
--
ALTER TABLE `auth_app_user_user_permissions`
  ADD CONSTRAINT `auth_app_user_user_p_permission_id_cc1b2396_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_app_user_user_p_user_id_b7c37328_fk_auth_app_` FOREIGN KEY (`user_id`) REFERENCES `auth_app_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `charges_charge`
--
ALTER TABLE `charges_charge`
  ADD CONSTRAINT `charges_charge_immeuble_id_d08ad9fa_fk_immeubles_immeuble_id` FOREIGN KEY (`immeuble_id`) REFERENCES `immeubles_immeuble` (`id`),
  ADD CONSTRAINT `charges_charge_local_id_2300d9db_fk_locaux_local_id` FOREIGN KEY (`local_id`) REFERENCES `locaux_local` (`id`);

--
-- Constraints for table `chat_groupchat`
--
ALTER TABLE `chat_groupchat`
  ADD CONSTRAINT `chat_groupchat_immeuble_id_e831694e_fk_immeubles_immeuble_id` FOREIGN KEY (`immeuble_id`) REFERENCES `immeubles_immeuble` (`id`),
  ADD CONSTRAINT `chat_groupchat_proprietaire_id_2d7dba35_fk_proprieta` FOREIGN KEY (`proprietaire_id`) REFERENCES `proprietaires_proprietaire` (`id`);

--
-- Constraints for table `chat_groupmessage`
--
ALTER TABLE `chat_groupmessage`
  ADD CONSTRAINT `chat_groupmessage_auteur_id_6c435380_fk_auth_app_user_id` FOREIGN KEY (`auteur_id`) REFERENCES `auth_app_user` (`id`),
  ADD CONSTRAINT `chat_groupmessage_group_id_754429fc_fk_chat_groupchat_id` FOREIGN KEY (`group_id`) REFERENCES `chat_groupchat` (`id`);

--
-- Constraints for table `contrats_bordereauvirement`
--
ALTER TABLE `contrats_bordereauvirement`
  ADD CONSTRAINT `contrats_bordereauvi_contrat_societe_id_2f3d7d17_fk_contrats_` FOREIGN KEY (`contrat_societe_id`) REFERENCES `contrats_contratsociete` (`id`),
  ADD CONSTRAINT `contrats_bordereauvi_proprietaire_id_c2578159_fk_proprieta` FOREIGN KEY (`proprietaire_id`) REFERENCES `proprietaires_proprietaire` (`id`),
  ADD CONSTRAINT `contrats_bordereauvi_traite_par_id_3d0c6167_fk_auth_app_` FOREIGN KEY (`traite_par_id`) REFERENCES `auth_app_user` (`id`);

--
-- Constraints for table `contrats_contrat`
--
ALTER TABLE `contrats_contrat`
  ADD CONSTRAINT `contrats_contrat_local_id_12e3c315_fk_locaux_local_id` FOREIGN KEY (`local_id`) REFERENCES `locaux_local` (`id`),
  ADD CONSTRAINT `contrats_contrat_locataire_id_715d7cc6_fk_locataire` FOREIGN KEY (`locataire_id`) REFERENCES `locataires_locataire` (`id`);

--
-- Constraints for table `contrats_contratsociete`
--
ALTER TABLE `contrats_contratsociete`
  ADD CONSTRAINT `contrats_contratsoci_proprietaire_id_3dbb5fc2_fk_proprieta` FOREIGN KEY (`proprietaire_id`) REFERENCES `proprietaires_proprietaire` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_app_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_app_user` (`id`);

--
-- Constraints for table `immeubles_immeuble`
--
ALTER TABLE `immeubles_immeuble`
  ADD CONSTRAINT `immeubles_immeuble_proprietaire_id_f3a805ad_fk_proprieta` FOREIGN KEY (`proprietaire_id`) REFERENCES `proprietaires_proprietaire` (`id`);

--
-- Constraints for table `locaux_local`
--
ALTER TABLE `locaux_local`
  ADD CONSTRAINT `locaux_local_immeuble_id_d7d3aa78_fk_immeubles_immeuble_id` FOREIGN KEY (`immeuble_id`) REFERENCES `immeubles_immeuble` (`id`),
  ADD CONSTRAINT `locaux_local_proprietaire_id_fe20c28d_fk_proprieta` FOREIGN KEY (`proprietaire_id`) REFERENCES `proprietaires_proprietaire` (`id`);

--
-- Constraints for table `loyers_bordereau`
--
ALTER TABLE `loyers_bordereau`
  ADD CONSTRAINT `loyers_bordereau_locataire_id_95940405_fk_locataire` FOREIGN KEY (`locataire_id`) REFERENCES `locataires_locataire` (`id`),
  ADD CONSTRAINT `loyers_bordereau_loyer_id_902b5764_fk_loyers_loyer_id` FOREIGN KEY (`loyer_id`) REFERENCES `loyers_loyer` (`id`);

--
-- Constraints for table `loyers_loyer`
--
ALTER TABLE `loyers_loyer`
  ADD CONSTRAINT `loyers_loyer_contrat_id_11197a6d_fk_contrats_contrat_id` FOREIGN KEY (`contrat_id`) REFERENCES `contrats_contrat` (`id`),
  ADD CONSTRAINT `loyers_loyer_local_id_40e7d952_fk_locaux_local_id` FOREIGN KEY (`local_id`) REFERENCES `locaux_local` (`id`),
  ADD CONSTRAINT `loyers_loyer_locataire_id_eed01b7b_fk_locataires_locataire_id` FOREIGN KEY (`locataire_id`) REFERENCES `locataires_locataire` (`id`);

--
-- Constraints for table `loyers_paiement`
--
ALTER TABLE `loyers_paiement`
  ADD CONSTRAINT `loyers_paiement_created_by_id_5fcdb5fc_fk_auth_app_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_app_user` (`id`),
  ADD CONSTRAINT `loyers_paiement_loyer_id_60c19813_fk_loyers_loyer_id` FOREIGN KEY (`loyer_id`) REFERENCES `loyers_loyer` (`id`);

--
-- Constraints for table `notifications_notification`
--
ALTER TABLE `notifications_notification`
  ADD CONSTRAINT `notifications_notifi_destinataire_locatai_fce6358c_fk_locataire` FOREIGN KEY (`destinataire_locataire_id`) REFERENCES `locataires_locataire` (`id`),
  ADD CONSTRAINT `notifications_notifi_destinataire_proprie_ae10a113_fk_proprieta` FOREIGN KEY (`destinataire_proprietaire_id`) REFERENCES `proprietaires_proprietaire` (`id`),
  ADD CONSTRAINT `notifications_notification_loyer_id_c6e28362_fk_loyers_loyer_id` FOREIGN KEY (`loyer_id`) REFERENCES `loyers_loyer` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
