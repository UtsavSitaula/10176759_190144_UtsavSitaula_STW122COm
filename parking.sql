-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2020 at 09:03 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `parking`
--

-- --------------------------------------------------------

--
-- Table structure for table `parking`
--

CREATE TABLE `parking` (
  `id` int(11) NOT NULL,
  `Vechile_number` varchar(100) NOT NULL,
  `Owner_name` varchar(100) NOT NULL,
  `ID_number` varchar(100) NOT NULL,
  `Token_number` varchar(100) NOT NULL,
  `Date` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `parking`
--

INSERT INTO `parking` (`id`, `Vechile_number`, `Owner_name`, `ID_number`, `Token_number`, `Date`) VALUES
(14, '2244', 'indra sitaula', '00', '0015', '05-09'),
(17, '1744', 'Hari prasad luitel', '001 COM', '0000', '17th aug'),
(18, '2429', 'Ram subedi ', '005 A', '0000', '17th aug'),
(19, '4456', 'prasamsha Nepal', '155 A', '0000', '18h march'),
(20, '2456', 'saroj', '0000', '0014', 'july 6'),
(21, '2457', 'sameer', '0000', '0017', 'july 6'),
(22, '2488', 'saurav ', '0000', '0018', 'july 6'),
(23, '0148', 'mandira ', '114B', '0000', 'jan 1'),
(24, '0188', 'tej parsad ', '144B', '0000', 'jan 1'),
(25, '7895', 'sudip Chettrai', '44B', '0000', 'jan 1'),
(26, '7854', 'srawan ', '0000', '0014', 'jan 1'),
(27, '7521', 'itachi joshi', '0000', '0124', 'jan 1'),
(28, '4850', 'itachi uchiha ', '12A', '0000', 'jan 19');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'utsav', '123456'),
(2, 'prasamsha', '123'),
(3, 'indra', '123456789'),
(4, 'hari', '159'),
(5, 'prasamsha', '123456789'),
(6, 'saroz', '123'),
(7, 'nayan', 'guessme'),
(8, 'nayan', 'guessme'),
(9, 'samikshya', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `parking`
--
ALTER TABLE `parking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `parking`
--
ALTER TABLE `parking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
