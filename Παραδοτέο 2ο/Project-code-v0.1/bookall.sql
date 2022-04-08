-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2021 at 10:47 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookall`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `category_id` int(9) NOT NULL,
  `category_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `City_Id` int(9) NOT NULL,
  `City_Name` varchar(255) NOT NULL,
  `Postal_Code` varchar(255) NOT NULL,
  `Country_Id` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`City_Id`, `City_Name`, `Postal_Code`, `Country_Id`) VALUES
(11, 'Athens', '16541', 88);

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `Company_Id` int(9) NOT NULL,
  `Company_Name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `City_Id` int(9) NOT NULL,
  `Company_address` varchar(255) DEFAULT NULL,
  `Details` text DEFAULT NULL,
  `Is_Active` tinyint(1) DEFAULT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Surname` varchar(255) DEFAULT NULL,
  `SiteURL` varchar(255) DEFAULT NULL,
  `Contact_Number` int(100) NOT NULL,
  `Number_of_Compartments` int(150) DEFAULT NULL,
  `Food_Type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`Company_Id`, `Company_Name`, `Email`, `City_Id`, `Company_address`, `Details`, `Is_Active`, `Name`, `Surname`, `SiteURL`, `Contact_Number`, `Number_of_Compartments`, `Food_Type`) VALUES
(1, 'KappaKeepo', 'kappa13keepo@gmai.com', 11, 'ghsubg', 'fefnfiwngibnsdgnw0', NULL, 'Stavros', 'Alexiou', 'dbgfwig', 0, NULL, NULL),
(19, 'KappaKeppo', 'eleapao13@gmail.com', 11, 'Kyprou 48', 'ppp', NULL, 'Eleanna', 'Theodosiou', 'www.muhaha.com', 0, NULL, NULL),
(20, 'Pites', 'eleapao13@gmail.com', 11, 'hgidhfiaoh', 'sadsadasda', NULL, 'Eleanna', 'Th', 'dhgsghsdg', 0, NULL, 'rrr'),
(21, 'Pites2', 'eleapao13@gmail.com', 11, 'fsfafsa', 'fgghjkl', NULL, 'Eleanna', 'TH', 'dsafgghjj', 1234567890, NULL, 'Vromiko'),
(22, 'Pites3', 'eleapao13@gmail.com', 11, 'fghj', 'hjkloiuy', NULL, 'Eleanna', 'Th', 'https://www.google.com/', 1234567890, NULL, 'rr');

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE `country` (
  `Country_Id` int(9) NOT NULL,
  `Country_Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `country`
--

INSERT INTO `country` (`Country_Id`, `Country_Name`) VALUES
(1, 'Afghanistan'),
(2, 'Åland Islands'),
(3, 'Albania'),
(4, 'Algeria'),
(5, 'American Samoa'),
(6, 'Andorra'),
(7, 'Angola'),
(8, 'Anguilla'),
(9, 'Antarctica'),
(10, 'Antigua & Barbuda'),
(11, 'Argentina'),
(12, 'Armenia'),
(13, 'Aruba'),
(14, 'Australia'),
(15, 'Austria'),
(16, 'Azerbaijan'),
(17, 'Bahamas'),
(18, 'Bahrain'),
(19, 'Bangladesh'),
(20, 'Barbados'),
(21, 'Belarus'),
(22, 'Belgium'),
(23, 'Belize'),
(24, 'Benin'),
(25, 'Bermuda'),
(26, 'Bhutan'),
(27, 'Bolivia'),
(28, 'Bosnia & Herzegovina'),
(29, 'Botswana'),
(30, 'Bouvet Island'),
(31, 'Brazil'),
(32, 'British Indian Ocean Territory'),
(33, 'British Virgin Islands'),
(34, 'Brunei'),
(35, 'Bulgaria'),
(36, 'Burkina Faso'),
(37, 'Burundi'),
(38, 'Cambodia'),
(39, 'Cameroon'),
(40, 'Canada'),
(41, 'Cape Verde'),
(42, 'Caribbean Netherlands'),
(43, 'Cayman Islands'),
(44, 'Central African Republic'),
(45, 'Chad'),
(46, 'Chile'),
(47, 'China'),
(48, 'Christmas Island'),
(49, 'Cocos (Keeling) Islands'),
(50, 'Colombia'),
(51, 'Comoros'),
(52, 'Congo - Brazzaville'),
(53, 'Congo - Kinshasa'),
(54, 'Cook Islands'),
(55, 'Costa Rica'),
(56, 'Côte d’Ivoire'),
(57, 'Croatia'),
(58, 'Cuba'),
(59, 'Curaçao'),
(60, 'Cyprus'),
(61, 'Czechia'),
(62, 'Denmark'),
(63, 'Djibouti'),
(64, 'Dominica'),
(65, 'Dominican Republic'),
(66, 'Ecuador'),
(67, 'Egypt'),
(68, 'El Salvador'),
(69, 'Equatorial Guinea'),
(70, 'Eritrea'),
(71, 'Estonia'),
(72, 'Eswatini'),
(73, 'Ethiopia'),
(74, 'Falkland Islands'),
(75, 'Faroe Islands'),
(76, 'Fiji'),
(77, 'Finland'),
(78, 'France'),
(79, 'French Guiana'),
(80, 'French Polynesia'),
(81, 'French Southern Territories'),
(82, 'Gabon'),
(83, 'Gambia'),
(84, 'Georgia'),
(85, 'Germany'),
(86, 'Ghana'),
(87, 'Gibraltar'),
(88, 'Greece'),
(89, 'Greenland'),
(90, 'Grenada'),
(91, 'Guadeloupe'),
(92, 'Guam'),
(93, 'Guatemala'),
(94, 'Guernsey'),
(95, 'Guinea'),
(96, 'Guinea-Bissau'),
(97, 'Guyana'),
(98, 'Haiti'),
(99, 'Heard & McDonald Islands'),
(100, 'Honduras'),
(101, 'Hong Kong SAR China'),
(102, 'Hungary'),
(103, 'Iceland'),
(104, 'India'),
(105, 'Indonesia'),
(106, 'Iran'),
(107, 'Iraq'),
(108, 'Ireland'),
(109, 'Isle of Man'),
(110, 'Israel'),
(111, 'Italy'),
(112, 'Jamaica'),
(113, 'Japan'),
(114, 'Jersey'),
(115, 'Jordan'),
(116, 'Kazakhstan'),
(117, 'Kenya'),
(118, 'Kiribati'),
(119, 'Kuwait'),
(120, 'Kyrgyzstan'),
(121, 'Laos'),
(122, 'Latvia'),
(123, 'Lebanon'),
(124, 'Lesotho'),
(125, 'Liberia'),
(126, 'Libya'),
(127, 'Liechtenstein'),
(128, 'Lithuania'),
(129, 'Luxembourg'),
(130, 'Macao SAR China'),
(131, 'Madagascar'),
(132, 'Malawi'),
(133, 'Malaysia'),
(134, 'Maldives'),
(135, 'Mali'),
(136, 'Malta'),
(137, 'Marshall Islands'),
(138, 'Martinique'),
(139, 'Mauritania'),
(140, 'Mauritius'),
(141, 'Mayotte'),
(142, 'Mexico'),
(143, 'Micronesia'),
(144, 'Moldova'),
(145, 'Monaco'),
(146, 'Mongolia'),
(147, 'Montenegro'),
(148, 'Montserrat'),
(149, 'Morocco'),
(150, 'Mozambique'),
(151, 'Myanmar (Burma)'),
(152, 'Namibia'),
(153, 'Nauru'),
(154, 'Nepal'),
(155, 'Netherlands'),
(156, 'New Caledonia'),
(157, 'New Zealand'),
(158, 'Nicaragua'),
(159, 'Niger'),
(160, 'Nigeria'),
(161, 'Niue'),
(162, 'Norfolk Island'),
(163, 'North Korea'),
(164, 'North Macedonia'),
(165, 'Northern Mariana Islands'),
(166, 'Norway'),
(167, 'Oman'),
(168, 'Pakistan'),
(169, 'Palau'),
(170, 'Palestinian Territories'),
(171, 'Panama'),
(172, 'Papua New Guinea'),
(173, 'Paraguay'),
(174, 'Peru'),
(175, 'Philippines'),
(176, 'Pitcairn Islands'),
(177, 'Poland'),
(178, 'Portugal'),
(179, 'Puerto Rico'),
(180, 'Qatar'),
(181, 'Réunion'),
(182, 'Romania'),
(183, 'Russia'),
(184, 'Rwanda'),
(185, 'Samoa'),
(186, 'San Marino'),
(187, 'São Tomé & Príncipe'),
(188, 'Saudi Arabia'),
(189, 'Senegal'),
(190, 'Serbia'),
(191, 'Seychelles'),
(192, 'Sierra Leone'),
(193, 'Singapore'),
(194, 'Sint Maarten'),
(195, 'Slovakia'),
(196, 'Slovenia'),
(197, 'Solomon Islands'),
(198, 'Somalia'),
(199, 'South Africa'),
(200, 'South Georgia & South Sandwich Isla\r\nnds'),
(201, 'South Korea'),
(202, 'South Sudan'),
(203, 'Spain'),
(204, 'Sri Lanka'),
(205, 'St. Barthélemy'),
(206, 'St. Helena'),
(207, 'St. Kitts & Nevis'),
(208, 'St. Lucia'),
(209, 'St. Martin'),
(210, 'St. Pierre & Miquelon'),
(211, 'St. Vincent & Grenadines'),
(212, 'Sudan'),
(213, 'Suriname'),
(214, 'Svalbard & Jan Mayen'),
(215, 'Sweden'),
(216, 'Switzerland'),
(217, 'Syria'),
(218, 'Taiwan'),
(219, 'Tajikistan'),
(220, 'Tanzania'),
(221, 'Thailand'),
(222, 'Timor-Leste'),
(223, 'Togo'),
(224, 'Tokelau'),
(225, 'Tonga'),
(226, 'Trinidad & Tobago'),
(227, 'Tunisia'),
(228, 'Turkey'),
(229, 'Turkmenistan'),
(230, 'Turks & Caicos Islands'),
(231, 'Tuvalu'),
(232, 'U.S. Outlying Islands'),
(233, 'U.S. Virgin Islands'),
(234, 'Uganda'),
(235, 'Ukraine'),
(236, 'United Arab Emirates'),
(237, 'United Kingdom'),
(238, 'United States'),
(239, 'Uruguay'),
(240, 'Uzbekistan'),
(241, 'Vanuatu'),
(242, 'Vatican City'),
(243, 'Venezuela'),
(244, 'Vietnam'),
(245, 'Wallis & Futuna'),
(246, 'Western Sahara'),
(247, 'Yemen'),
(248, 'Zambia'),
(249, 'Zimbabwe');

-- --------------------------------------------------------

--
-- Table structure for table `hotel`
--

CREATE TABLE `hotel` (
  `Hotel_Id` int(9) NOT NULL,
  `Hotel_name` varchar(255) NOT NULL,
  `Description` text DEFAULT NULL,
  `company_id` int(9) NOT NULL,
  `city_id` int(9) NOT NULL,
  `category_id` int(9) NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `role_id` int(4) NOT NULL,
  `role_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`role_id`, `role_name`) VALUES
(0, 'client'),
(1, 'businessman');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `ID` int(9) NOT NULL,
  `room_name` varchar(255) NOT NULL,
  `Description` text DEFAULT NULL,
  `hotel_id` int(9) NOT NULL,
  `room_type_id` int(9) NOT NULL,
  `current_price` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `room_type`
--

CREATE TABLE `room_type` (
  `room_id` int(9) NOT NULL,
  `type_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UsersId` int(11) NOT NULL,
  `Usersusername` varchar(255) NOT NULL,
  `Usersemail` varchar(255) NOT NULL,
  `Userspwd` varchar(255) NOT NULL,
  `company_id` int(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UsersId`, `Usersusername`, `Usersemail`, `Userspwd`, `company_id`) VALUES
(10, 'dimos', 'dimmin99@gmail.com', '8a020c7b0bbef63dfb316448b8d98a4d27a8a4beb3e749a0756e692007df4ac14c4194926773a17de58c8ae7ac7d4ca9078bd7f6db598c2f3813f2df49d9157f06aaa8fcb156c91227190375ac64782173b3cac63e89c47d0068f4a8cb00ac9d', NULL),
(11, 'Eleanna', 'eleannoubi26@gmail.com', 'd3a9a694c34b5cb309124baa87c3975a5d90dba1a53660dd878fcbabeccb879681fb8814b007653638bac3d130cec2d95178e69809a982768d8a30cc829380e693c41e5910fab82a10854938a242925cd8a0fd0e96090e79130fe74629b405bf', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user_roles`
--

CREATE TABLE `user_roles` (
  `user_id` int(9) NOT NULL,
  `role_id` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_roles`
--

INSERT INTO `user_roles` (`user_id`, `role_id`) VALUES
(10, 0),
(11, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`City_Id`),
  ADD KEY `CITIES` (`Country_Id`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`Company_Id`),
  ADD KEY `CITY` (`City_Id`);

--
-- Indexes for table `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`Country_Id`);

--
-- Indexes for table `hotel`
--
ALTER TABLE `hotel`
  ADD PRIMARY KEY (`Hotel_Id`),
  ADD KEY `GTXM` (`company_id`),
  ADD KEY `GTXT` (`city_id`),
  ADD KEY `GTXS` (`category_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CON` (`hotel_id`),
  ADD KEY `CON1` (`room_type_id`);

--
-- Indexes for table `room_type`
--
ALTER TABLE `room_type`
  ADD PRIMARY KEY (`room_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UsersId`),
  ADD KEY `FK_company` (`company_id`);

--
-- Indexes for table `user_roles`
--
ALTER TABLE `user_roles`
  ADD PRIMARY KEY (`user_id`,`role_id`),
  ADD KEY `Role_cstr` (`role_id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `City_Id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `Company_Id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `country`
--
ALTER TABLE `country`
  MODIFY `Country_Id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=250;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `UsersId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `CITIES` FOREIGN KEY (`Country_Id`) REFERENCES `country` (`Country_Id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `company`
--
ALTER TABLE `company`
  ADD CONSTRAINT `CITY` FOREIGN KEY (`City_Id`) REFERENCES `city` (`City_Id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `hotel`
--
ALTER TABLE `hotel`
  ADD CONSTRAINT `GTXM` FOREIGN KEY (`company_id`) REFERENCES `company` (`Company_Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `GTXS` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `GTXT` FOREIGN KEY (`city_id`) REFERENCES `city` (`City_Id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `room`
--
ALTER TABLE `room`
  ADD CONSTRAINT `CON` FOREIGN KEY (`hotel_id`) REFERENCES `hotel` (`Hotel_Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `CON1` FOREIGN KEY (`room_type_id`) REFERENCES `room_type` (`room_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `FK_company` FOREIGN KEY (`company_id`) REFERENCES `company` (`Company_Id`);

--
-- Constraints for table `user_roles`
--
ALTER TABLE `user_roles`
  ADD CONSTRAINT `Role_cstr` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `User_cstr` FOREIGN KEY (`user_id`) REFERENCES `users` (`UsersId`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
