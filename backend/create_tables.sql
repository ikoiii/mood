-- =====================================================
-- Mood and Pain Tracker Database Schema
-- =====================================================
-- Database: mood_tracker
-- Engine: MySQL (XAMPP)

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS mood_tracker;
USE mood_tracker;

-- Drop tables if they exist (for fresh start)
DROP TABLE IF EXISTS entries;
DROP TABLE IF EXISTS patients;

-- =====================================================
-- Table: patients
-- =====================================================
-- Menyimpan data pasien yang akan menggunakan QR code login
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    room VARCHAR(20) NOT NULL,
    qr_token VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Index untuk QR token lookup
    INDEX idx_qr_token (qr_token),

    -- Index untuk room lookup
    INDEX idx_room (room)
);

-- =====================================================
-- Table: entries
-- =====================================================
-- Menyimpan data mood dan pain level dari pasien
CREATE TABLE entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    mood VARCHAR(50) NOT NULL,
    pain_level INT NOT NULL CHECK (pain_level >= 0 AND pain_level <= 10),
    note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Foreign key constraint
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,

    -- Index untuk patient lookup
    INDEX idx_patient_id (patient_id),

    -- Index untuk created_at (untuk filtering berdasarkan waktu)
    INDEX idx_created_at (created_at)
);

-- =====================================================
-- Insert Sample Data (Optional - untuk testing)
-- =====================================================

-- Sample patient data
INSERT INTO patients (name, age, room, qr_token) VALUES
('John Doe', 45, 'Room 101', 'QR_TOKEN_001'),
('Jane Smith', 32, 'Room 102', 'QR_TOKEN_002'),
('Ahmad Rizki', 28, 'Room 103', 'QR_TOKEN_003');

-- Sample entry data
INSERT INTO entries (patient_id, mood, pain_level, note) VALUES
(1, 'happy', 3, 'Feeling good today'),
(2, 'neutral', 5, 'Moderate pain'),
(3, 'sad', 7, 'Pain increased after therapy');

-- =====================================================
-- Views (Optional - untuk query yang sering digunakan)
-- =====================================================

-- View untuk menampilkan semua entries dengan patient info
CREATE VIEW patient_entries AS
SELECT
    e.id as entry_id,
    p.name as patient_name,
    p.room as patient_room,
    e.mood,
    e.pain_level,
    e.note,
    e.created_at as entry_time
FROM entries e
JOIN patients p ON e.patient_id = p.id
ORDER BY e.created_at DESC;

-- =====================================================
-- Stored Procedures (Optional - untuk operasi kompleks)
-- =====================================================

-- Procedure untuk get latest entry per patient
DELIMITER //
CREATE PROCEDURE GetLatestEntryPerPatient()
BEGIN
    SELECT
        p.id as patient_id,
        p.name as patient_name,
        p.room,
        e.mood as latest_mood,
        e.pain_level as latest_pain_level,
        e.created_at as latest_entry_time
    FROM patients p
    LEFT JOIN entries e ON p.id = e.patient_id
    WHERE e.id = (
        SELECT MAX(e2.id)
        FROM entries e2
        WHERE e2.patient_id = p.id
    )
    ORDER BY p.name;
END //
DELIMITER ;

-- =====================================================
-- Query Examples
-- =====================================================

-- 1. Get all patients
-- SELECT * FROM patients ORDER BY created_at DESC;

-- 2. Get all entries for a specific patient
-- SELECT * FROM entries WHERE patient_id = 1 ORDER BY created_at DESC;

-- 3. Get entries from last 24 hours
-- SELECT * FROM entries WHERE created_at >= DATE_SUB(NOW(), INTERVAL 1 DAY);

-- 4. Get average pain level per patient
-- SELECT p.name, AVG(e.pain_level) as avg_pain
-- FROM patients p
-- JOIN entries e ON p.id = e.patient_id
-- GROUP BY p.id, p.name;

-- 5. Get mood distribution
-- SELECT mood, COUNT(*) as count
-- FROM entries
-- GROUP BY mood
-- ORDER BY count DESC;

-- =====================================================
-- Database Setup Complete!
-- =====================================================