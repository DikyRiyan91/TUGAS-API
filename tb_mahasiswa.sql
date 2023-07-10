-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 10, 2023 at 08:40 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `learn_api_graphql`
--

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `nim_mhs` int NOT NULL,
  `nama_lengkap` varchar(100) NOT NULL,
  `program_studi` enum('TI','SI','DKV') NOT NULL,
  `no_telepon` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`nim_mhs`, `nama_lengkap`, `program_studi`, `no_telepon`) VALUES
(12345678, 'Ava Martinez', 'TI', '090123456789'),
(123456789, 'John Doe', 'TI', '081234567890'),
(234567890, 'Jane Smith', 'SI', '082345678901'),
(345678901, 'David Johnson', 'DKV', '083456789012'),
(456789012, 'Emily Williams', 'TI', '084567890123'),
(567890123, 'Michael Brown', 'SI', '085678901234'),
(678901234, 'Sophia Davis', 'DKV', '086789012345'),
(789012345, 'Oliver Miller', 'TI', '087890123456'),
(890123456, 'Emma Wilson', 'SI', '088901234567'),
(901234567, 'Noah Anderson', 'DKV', '089012345678');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`nim_mhs`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
