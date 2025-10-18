--Sample Database just to test

CREATE DATABASE IF NOT EXISTS grid_forecast;
USE grid_forecast;

-- 1. Zones table
CREATE TABLE zones (
    zone_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    zone_name VARCHAR(50) NOT NULL,
    region_code VARCHAR(10) UNIQUE
);

-- 2. Electricity data
CREATE TABLE electricity_data (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    zone_id BIGINT UNSIGNED,
    date_time TIMESTAMP NOT NULL,
    actual_demand FLOAT,
    predicted_demand FLOAT,
    unit VARCHAR(10) DEFAULT 'MW',
    source VARCHAR(50) DEFAULT 'Kaggle',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (zone_id) REFERENCES zones(zone_id)
);

-- 3. Weather data
CREATE TABLE weather_data (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    zone_id BIGINT UNSIGNED,
    date_time TIMESTAMP NOT NULL,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    solar_radiation FLOAT,
    source VARCHAR(50) DEFAULT 'OpenWeather',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (zone_id) REFERENCES zones(zone_id)
);

-- 4. Holidays table
CREATE TABLE holidays (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    name VARCHAR(100),
    country VARCHAR(50),
    type VARCHAR(50),
    is_festival TINYINT(1) DEFAULT 0,
    source VARCHAR(50) DEFAULT 'Calendarific'
);

-- 5. Forecast results
CREATE TABLE forecast_results (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    model_name VARCHAR(50),
    version VARCHAR(20),
    mae FLOAT,
    rmse FLOAT,
    mape FLOAT,
    wape FLOAT,
    trained_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Alerts table
CREATE TABLE alerts (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    zone_id BIGINT UNSIGNED,
    alert_level ENUM('Normal', 'Warning', 'Critical'),
    message TEXT,
    forecast_time TIMESTAMP,
    triggered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (zone_id) REFERENCES zones(zone_id)
);

-- 7. SOS logs
CREATE TABLE sos_logs (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    alert_id BIGINT UNSIGNED,
    triggered_by VARCHAR(50),
    call_status VARCHAR(20) DEFAULT 'Pending',
    call_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (alert_id) REFERENCES alerts(id)
);

-- 8. Users table
CREATE TABLE users (
    user_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    role VARCHAR(50) DEFAULT 'operator',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO zones (zone_name, region_code) VALUES
('North Zone', 'NZ01'),
('South Zone', 'SZ02'),
('East Zone', 'EZ03'),
('West Zone', 'WZ04');

INSERT INTO weather_data (zone_id, date_time, temperature, humidity, wind_speed, solar_radiation)
VALUES
(1, '2025-10-15 00:00:00', 27.5, 65.0, 10.5, 180.3),
(2, '2025-10-15 00:00:00', 30.2, 70.2, 12.1, 190.6),
(3, '2025-10-15 00:00:00', 25.8, 60.5, 9.0, 170.1),
(4, '2025-10-15 00:00:00', 28.0, 68.3, 11.2, 185.7);

INSERT INTO holidays (date, name, country, type, is_festival)
VALUES
('2025-01-26', 'Republic Day', 'India', 'National Holiday', 1),
('2025-08-15', 'Independence Day', 'India', 'National Holiday', 1),
('2025-10-02', 'Gandhi Jayanti', 'India', 'National Holiday', 1);

INSERT INTO forecast_results (model_name, version, mae, rmse, mape, wape)
VALUES
('LSTM-Predictor', 'v1.2', 45.23, 60.45, 3.8, 2.1),
('RandomForest-Regressor', 'v1.0', 52.11, 68.75, 4.3, 2.5);

INSERT INTO users (name, email, role)
VALUES
('Admin User', 'admin@gridforecast.in', 'admin'),
('Operator 1', 'operator1@gridforecast.in', 'operator'),
('Analyst', 'analyst@gridforecast.in', 'data_analyst');

SELECT * 
FROM zones;

SELECT ed.id, z.zone_name, ed.date_time, ed.actual_demand, ed.predicted_demand, ed.unit, ed.source
FROM electricity_data ed
JOIN zones z ON ed.zone_id = z.zone_id
ORDER BY ed.date_time;

SELECT wd.id, z.zone_name, wd.date_time, wd.temperature, wd.humidity, wd.wind_speed, wd.solar_radiation, wd.source
FROM weather_data wd
JOIN zones z ON wd.zone_id = z.zone_id
ORDER BY wd.date_time;

SELECT a.id, z.zone_name, a.alert_level, a.message, a.forecast_time, a.triggered_at
FROM alerts a
JOIN zones z ON a.zone_id = z.zone_id
ORDER BY a.triggered_at DESC;

SELECT z.zone_name, ed.date_time, ed.actual_demand, ed.predicted_demand
FROM electricity_data ed
JOIN zones z ON ed.zone_id = z.zone_id
WHERE z.zone_name = 'North Zone'
ORDER BY ed.date_time;


