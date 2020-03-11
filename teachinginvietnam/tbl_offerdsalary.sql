-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th1 10, 2020 lúc 12:14 PM
-- Phiên bản máy phục vụ: 10.3.16-MariaDB
-- Phiên bản PHP: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `teachinginvietnam`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `tbl_offerdsalary`
--

CREATE TABLE `tbl_offerdsalary` (
  `ID` int(11) NOT NULL,
  `Description` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `tbl_offerdsalary`
--

INSERT INTO `tbl_offerdsalary` (`ID`, `Description`) VALUES
(1, '$10 -$12 / Hour '),
(2, '$12 – $15 / Hour '),
(3, '$15 – $18 / Hour '),
(4, '$18 – $25 / Hour '),
(5, '$25 plus / Hour '),
(6, '$30 plus / hour '),
(7, '0 -  $500 '),
(8, '$500 - $1000 '),
(9, '$1000 - $1500 '),
(10, '$1500 - $2000 '),
(11, '$2000 – $2500 '),
(12, '$2500 – $3000 '),
(13, '$3000 – $3500 (0)'),
(14, '$3500 – $4000 '),
(15, '$4000 – $4500 '),
(16, '$4500 – $5000 ');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `tbl_offerdsalary`
--
ALTER TABLE `tbl_offerdsalary`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `tbl_offerdsalary`
--
ALTER TABLE `tbl_offerdsalary`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
