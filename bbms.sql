-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2021 at 03:25 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bbms`
--

-- --------------------------------------------------------

--
-- Table structure for table `blood`
--

CREATE TABLE `blood` (
  `Blood_Group` varchar(5) NOT NULL,
  `Donate_Blood_To` varchar(50) DEFAULT NULL,
  `Receive_Blood_From` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blood`
--

INSERT INTO `blood` (`Blood_Group`, `Donate_Blood_To`, `Receive_Blood_From`) VALUES
('A+', 'A+,AB+', 'A+,A-,O+,O-'),
('A-', 'A+,A-,AB+,AB-', 'A-,O-'),
('AB+', 'AB+', 'Everyone'),
('AB-', 'AB+,AB-', 'AB-,A-,B-,O-'),
('B+', 'B+,AB+', 'B+,B-,O+,O-'),
('O+', 'O+,A+,B+,AB+', 'O+,O-'),
('O-', 'Everyone', 'O-');

-- --------------------------------------------------------

--
-- Table structure for table `donor`
--

CREATE TABLE `donor` (
  `D_Id` varchar(50) NOT NULL,
  `D_Name` varchar(50) DEFAULT NULL,
  `D_Blood_Group` varchar(5) DEFAULT NULL,
  `D_Age` varchar(5) DEFAULT NULL,
  `D_Gender` varchar(10) DEFAULT NULL,
  `D_Phone` varchar(20) DEFAULT NULL,
  `D_Last_Donate` varchar(20) DEFAULT NULL,
  `D_Next_Donate` varchar(20) DEFAULT NULL,
  `D_Address` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `donor`
--

INSERT INTO `donor` (`D_Id`, `D_Name`, `D_Blood_Group`, `D_Age`, `D_Gender`, `D_Phone`, `D_Last_Donate`, `D_Next_Donate`, `D_Address`) VALUES
('D-010', 'Sharthok Saha', 'AB+', '22', 'Male', '01954431549', '19-04-2020', '20-07-2020', 'Dhaka'),
('D-011', 'Rafika Auddry', 'A+', '21', 'Female', '01977284073', '15-10-2020', '16-01-2021', 'Dhaka'),
('D-012', 'Arpita Saha Api', 'B+', '20', 'Female', '01567234567', '07-01-2021', '08-04-2021', 'Dhaka'),
('D-013', 'Anwar Hossain', 'O+', '23', 'Male', '01941195020', '12-01-2021', '13-04-2021', 'Dhaka'),
('D-014', 'Mahjabin Binte Kabir', 'B+', '21', 'Female', '01987656789', '12-10-2020', '13-01-2021', 'Tangail'),
('D-015', 'Mohaiminul Mubin', 'A+', '22', 'Male', '01789878678', '25-02-2021', '26-05-2021', 'Dhaka'),
('D-016', 'Tania Akter Ria', 'A-', '21', 'Female', '01567768909', '02-03-2021', '03-06-2021', 'Laxmipur'),
('D-017', 'Imdadul Haque Imran ', 'AB+', '23', 'Male', '01567854345', '05-12-2020', '06-03-2021', 'Cumilla'),
('D-018', 'Mahadi Rahman Dhrubo', 'AB+', '21', 'Male', '01789123456', '30-01-2021', '01-05-2021', 'Candpur'),
('D-019', 'Sadia Islam', 'A+', '21', 'Female', '01786654563', '15-12-2020', '16-03-2021', 'Pabna'),
('D-020', 'Sadia Afrin Jhilik', 'O+', '21', 'Female', '01567898453', '20-03-2021', '21-06-2021', 'Dhaka'),
('D-021', 'Hridita Saha', 'A+', '25', 'Female', '01672244971', '20-03-2021', '21-06-2021', 'Barishal'),
('D-022', 'Ritu Saha', 'O-', '30', 'Female', '01564323456', '10-05-2020', '11-08-2020', 'Barishal'),
('D-023', 'Rohit Shil', 'B+', '29', 'Male', '01654323466', '06-01-2020', '07-04-2020', 'Chittagang'),
('D-024', 'Zamiar Hossain', 'AB-', '30', 'Male', '01756432345', '12-02-2021', '13-03-2021', 'Barishal'),
('D-025', 'Naima Khandakar', 'AB+', '29', 'Female', '01898787865', '13-05-2020', '14-08-2020', 'Dhaka'),
('D-026', 'Debobroto Chakroborty', 'O+', '24', 'Male', '01609876543', '18-09-2020', '19-12-2020', 'Savar'),
('D-027', 'Joyeeta Chakroborty', 'O-', '21', 'Female', '01812342345', '28-02-2021', '29-05-2021', 'Dhaka');

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `Stock_id` varchar(50) NOT NULL,
  `Blood_Group` varchar(5) DEFAULT NULL,
  `Stock_status` varchar(50) DEFAULT NULL,
  `Stock_Quantity` varchar(50) DEFAULT NULL,
  `Hospital_Name` varchar(200) DEFAULT NULL,
  `Hospital_Address` varchar(200) DEFAULT NULL,
  `Hospital_Phone` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`Stock_id`, `Blood_Group`, `Stock_status`, `Stock_Quantity`, `Hospital_Name`, `Hospital_Address`, `Hospital_Phone`) VALUES
('S-010', 'O+', 'Availavle', '05', 'Dhaka Medical College', 'Bakshibazar,Dhaka', '02-956789'),
('S-011', 'O-', 'Not Availavle', '00', 'Dhaka Medical College', 'Bakshibazar,Dhaka', '02-956789'),
('S-012', 'AB+', 'Availavle', '06', 'Dhaka Medical College', 'Bakshibazar,Dhaka', '02-956789'),
('S-013', 'AB-', 'Not Availavle', '00', 'Dhaka Medical College', 'Bakshibazar,Dhaka', '02-956789'),
('S-014', 'A+', 'Availavle', '10', 'Dhaka Medical College', 'Bakshibazar,Dhaka', '02-956789'),
('S-015', 'A-', 'Not Availavle', '00', 'Dhaka Medical College', 'Bakshibazar,Dhaka', '02-956789'),
('S-016', 'B+', 'Availavle', '02', 'Dhaka Medical College', 'Bakshibazar,Dhaka', '02-956789'),
('S-017', 'B-', 'Availavle', '02', 'Dhaka Medical College', 'Bakshibazar,Dhaka', '02-956789'),
('S-111', 'A+', 'Availavle', '08', 'Labaid Specialized Hospital', 'Dhanmondi,Dhaka', '02-126789'),
('S-112', 'A-', 'Availavle', '04', 'Labaid Specialized Hospital', 'Dhanmondi,Dhaka', '02-126789'),
('S-113', 'B+', 'Availavle', '15', 'Labaid Specialized Hospital', 'Dhanmondi,Dhaka', '02-126789'),
('S-114', 'B-', 'Not Availavle', '00', 'Labaid Specialized Hospital', 'Dhanmondi,Dhaka', '02-126789'),
('S-115', 'O+', 'Availavle', '07', 'Labaid Specialized Hospital', 'Dhanmondi,Dhaka', '02-126789'),
('S-116', 'O-', 'Not Availavle', '00', 'Labaid Specialized Hospital', 'Dhanmondi,Dhaka', '02-126789'),
('S-117', 'AB+', 'Availavle', '20', 'Labaid Specialized Hospital', 'Dhanmondi,Dhaka', '02-126789'),
('S-118', 'AB-', 'Availavle', '03', 'Labaid Specialized Hospital', 'Dhanmondi,Dhaka', '02-126789'),
('S-119', 'A+', 'Availavle', '3', 'Anwer Khan Modern', 'Kalabagan,Dhanmondi', '02-345678');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blood`
--
ALTER TABLE `blood`
  ADD PRIMARY KEY (`Blood_Group`);

--
-- Indexes for table `donor`
--
ALTER TABLE `donor`
  ADD PRIMARY KEY (`D_Id`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`Stock_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
