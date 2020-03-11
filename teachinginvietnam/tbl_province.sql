-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th1 10, 2020 lúc 12:20 PM
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
-- Cơ sở dữ liệu: `quan_huyen`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `tbl_province`
--

CREATE TABLE `tbl_province` (
  `Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `ID_Province` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Đang đổ dữ liệu cho bảng `tbl_province`
--

INSERT INTO `tbl_province` (`Name`, `ID_Province`) VALUES
('Thành phố Hà Nội', 1),
('Tỉnh Hà Giang', 2),
('Tỉnh Cao Bằng', 4),
('Tỉnh Bắc Kạn', 6),
('Tỉnh Tuyên Quang', 8),
('Tỉnh Lào Cai', 10),
('Tỉnh Điện Biên', 11),
('Tỉnh Lai Châu', 12),
('Tỉnh Sơn La', 14),
('Tỉnh Yên Bái', 15),
('Tỉnh Hoà Bình', 17),
('Tỉnh Thái Nguyên', 19),
('Tỉnh Lạng Sơn', 20),
('Tỉnh Quảng Ninh', 22),
('Tỉnh Bắc Giang', 24),
('Tỉnh Phú Thọ', 25),
('Tỉnh Vĩnh Phúc', 26),
('Tỉnh Bắc Ninh', 27),
('Tỉnh Hải Dương', 30),
('Thành phố Hải Phòng', 31),
('Tỉnh Hưng Yên', 33),
('Tỉnh Thái Bình', 34),
('Tỉnh Hà Nam', 35),
('Tỉnh Nam Định', 36),
('Tỉnh Ninh Bình', 37),
('Tỉnh Thanh Hóa', 38),
('Tỉnh Nghệ An', 40),
('Tỉnh Hà Tĩnh', 42),
('Tỉnh Quảng Bình', 44),
('Tỉnh Quảng Trị', 45),
('Tỉnh Thừa Thiên Huế', 46),
('Thành phố Đà Nẵng', 48),
('Tỉnh Quảng Nam', 49),
('Tỉnh Quảng Ngãi', 51),
('Tỉnh Bình Định', 52),
('Tỉnh Phú Yên', 54),
('Tỉnh Khánh Hòa', 56),
('Tỉnh Ninh Thuận', 58),
('Tỉnh Bình Thuận', 60),
('Tỉnh Kon Tum', 62),
('Tỉnh Gia Lai', 64),
('Tỉnh Đắk Lắk', 66),
('Tỉnh Đắk Nông', 67),
('Tỉnh Lâm Đồng', 68),
('Tỉnh Bình Phước', 70),
('Tỉnh Tây Ninh', 72),
('Tỉnh Bình Dương', 74),
('Tỉnh Đồng Nai', 75),
('Tỉnh Bà Rịa - Vũng Tàu', 77),
('Thành phố Hồ Chí Minh', 79),
('Tỉnh Long An', 80),
('Tỉnh Tiền Giang', 82),
('Tỉnh Bến Tre', 83),
('Tỉnh Trà Vinh', 84),
('Tỉnh Vĩnh Long', 86),
('Tỉnh Đồng Tháp', 87),
('Tỉnh An Giang', 89),
('Tỉnh Kiên Giang', 91),
('Thành phố Cần Thơ', 92),
('Tỉnh Hậu Giang', 93),
('Tỉnh Sóc Trăng', 94),
('Tỉnh Bạc Liêu', 95),
('Tỉnh Cà Mau', 96);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
