-- 1) Limpiar esquema (orden de drops: vistas → tablas dependientes → tablas base)
DROP VIEW IF EXISTS asistencia_mensual;

DROP TABLE IF EXISTS asistencia_dia;
DROP TABLE IF EXISTS cuenta_deposito;
DROP TABLE IF EXISTS tipos_cuenta;
DROP TABLE IF EXISTS bancos;

DROP TABLE IF EXISTS contrato;
DROP TABLE IF EXISTS proyectos;
DROP TABLE IF EXISTS empleados;
DROP TABLE IF EXISTS estados_civil;
DROP TABLE IF EXISTS sistemas_salud;
DROP TABLE IF EXISTS afp;


-- 2) Tablas de catálogo básicas

CREATE TABLE afp (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE sistemas_salud (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE estados_civil (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(20) UNIQUE NOT NULL
);


-- 3) Catálogos para cuentas bancarias

CREATE TABLE bancos (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE tipos_cuenta (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(50) UNIQUE NOT NULL
);


-- 4) Tabla de empleados (sin booleano de depósito)

CREATE TABLE empleados (
  id                SERIAL PRIMARY KEY,
  nombre            VARCHAR(120) NOT NULL,
  rut               VARCHAR(12) UNIQUE NOT NULL,
  correo_trabajador TEXT UNIQUE,
  fecha_nacimiento  DATE NOT NULL,
  estado_civil_id   INT REFERENCES estados_civil(id)
);


-- 5) Proyectos y contratos

CREATE TABLE proyectos (
  id            SERIAL PRIMARY KEY,
  nombre        VARCHAR(150) UNIQUE NOT NULL,
  fecha_inicio  DATE,
  fecha_termino DATE
);

CREATE TABLE contrato (
  id                SERIAL PRIMARY KEY,
  empleado_id       INT UNIQUE NOT NULL REFERENCES empleados(id),
  proyecto_id       INT NOT NULL REFERENCES proyectos(id),
  fecha_ingreso     DATE NOT NULL,
  afp_id            INT REFERENCES afp(id),
  sistema_salud_id  INT REFERENCES sistemas_salud(id),
  telefono_emp      VARCHAR(15),
  correo_empl       TEXT,
  sueldo_diario     NUMERIC(10,2),
  created_at        TIMESTAMPTZ DEFAULT now(),
  updated_at        TIMESTAMPTZ DEFAULT now()
);


-- 6) Asociación Empleado ↔ Cuenta de Depósito

CREATE TABLE cuenta_deposito (
  id             SERIAL PRIMARY KEY,
  empleado_id    INT NOT NULL UNIQUE REFERENCES empleados(id),
  banco_id       INT NOT NULL REFERENCES bancos(id),
  tipo_cuenta_id INT NOT NULL REFERENCES tipos_cuenta(id),
  numero_cuenta  VARCHAR(30) NOT NULL
);


-- 7) Inserción de datos de ejemplo para pruebas
-- ORDEN CORRECTO: Primero tablas padre, luego tablas dependientes
-- USAR ON CONFLICT para evitar duplicados

-- 1) Insertar Estados Civiles (PRIMERO - tabla padre)
INSERT INTO estados_civil (nombre) VALUES 
('Soltero'),
('Casado'),
('Divorciado'),
('Viudo'),
('Conviviente')
ON CONFLICT (nombre) DO NOTHING;

-- 2) Insertar AFPs
INSERT INTO afp (nombre) VALUES 
('Provida'),
('Habitat'),
('Cuprum'),
('Capital'),
('PlanVital'),
('Modelo'),
('UNO')
ON CONFLICT (nombre) DO NOTHING;

-- 3) Insertar Sistemas de Salud
INSERT INTO sistemas_salud (nombre) VALUES 
('Fonasa'),
('Isapre Banmedica'),
('Isapre Cruz Blanca'),
('Isapre Consalud'),
('Isapre Vida Tres'),
('Isapre Colmena')
ON CONFLICT (nombre) DO NOTHING;

-- 4) Insertar Bancos
INSERT INTO bancos (nombre) VALUES 
('Banco de Chile'),
('Banco Estado'),
('Banco Santander'),
('BCI'),
('Banco Security'),
('Banco Falabella'),
('Scotiabank')
ON CONFLICT (nombre) DO NOTHING;

-- 5) Insertar Tipos de Cuenta
INSERT INTO tipos_cuenta (nombre) VALUES 
('Cuenta Corriente'),
('Cuenta Vista'),
('Cuenta de Ahorro'),
('Cuenta RUT')
ON CONFLICT (nombre) DO NOTHING;

-- 6) Insertar Proyectos
INSERT INTO proyectos (nombre, fecha_inicio, fecha_termino) VALUES 
('Proyecto Edificio Central', '2025-01-15', '2025-12-31'),
('Construcción Mall Las Condes', '2025-02-01', '2026-01-31'),
('Remodelación Hospital', '2025-03-01', '2025-11-30'),
('Torre Residencial Norte', '2025-01-10', '2025-10-15'),
('Centro Comercial Sur', '2025-04-01', '2026-03-31')
ON CONFLICT (nombre) DO NOTHING;

-- 7) Insertar Empleados (DESPUÉS de estados_civil)
INSERT INTO empleados (nombre, rut, correo_trabajador, fecha_nacimiento, estado_civil_id) VALUES 
('Juan Carlos Pérez González', '12345678-9', 'juan.perez@cubicanet.cl', '1985-03-15', 2),
('María Elena Rodriguez Silva', '23456789-0', 'maria.rodriguez@cubicanet.cl', '1990-07-22', 1),
('Carlos Alberto Mendoza Torres', '34567890-1', 'carlos.mendoza@cubicanet.cl', '1988-11-08', 2),
('Ana Patricia López Vera', '45678901-2', 'ana.lopez@cubicanet.cl', '1992-01-30', 3),
('Luis Fernando Castro Morales', '56789012-3', 'luis.castro@cubicanet.cl', '1987-09-12', 1),
('Carmen Rosa Herrera Díaz', '67890123-4', 'carmen.herrera@cubicanet.cl', '1991-05-18', 2),
('Roberto Miguel Vargas Flores', '78901234-5', 'roberto.vargas@cubicanet.cl', '1989-12-03', 1),
('Sofía Alejandra Muñoz Ramos', '89012345-6', 'sofia.munoz@cubicanet.cl', '1993-08-25', 1)
ON CONFLICT (rut) DO NOTHING;

-- 8) Insertar Contratos (DESPUÉS de empleados, proyectos, afp, sistemas_salud)
INSERT INTO contrato (empleado_id, proyecto_id, fecha_ingreso, afp_id, sistema_salud_id, telefono_emp, correo_empl, sueldo_diario) VALUES 
(1, 1, '2025-01-20', 1, 1, '+56912345678', 'juan.perez@personal.cl', 45000.00),
(2, 1, '2025-02-01', 2, 2, '+56923456789', 'maria.rodriguez@personal.cl', 42000.00),
(3, 2, '2025-02-10', 3, 1, '+56934567890', 'carlos.mendoza@personal.cl', 48000.00),
(4, 2, '2025-02-15', 1, 3, '+56945678901', 'ana.lopez@personal.cl', 40000.00),
(5, 3, '2025-03-05', 4, 1, '+56956789012', 'luis.castro@personal.cl', 46000.00),
(6, 3, '2025-03-10', 2, 4, '+56967890123', 'carmen.herrera@personal.cl', 44000.00),
(7, 4, '2025-01-25', 5, 1, '+56978901234', 'roberto.vargas@personal.cl', 47000.00),
(8, 5, '2025-04-05', 3, 5, '+56989012345', 'sofia.munoz@personal.cl', 43000.00)
ON CONFLICT (empleado_id) DO NOTHING;

-- 9) Insertar Cuentas de Depósito (AL FINAL - después de empleados, bancos, tipos_cuenta)
INSERT INTO cuenta_deposito (empleado_id, banco_id, tipo_cuenta_id, numero_cuenta) VALUES 
(1, 1, 1, '12345678901234567890'),
(2, 2, 4, '23456789012345678901'),
(3, 3, 2, '34567890123456789012'),
(4, 1, 3, '45678901234567890123'),
(5, 4, 1, '56789012345678901234'),
(6, 2, 4, '67890123456789012345'),
(7, 5, 2, '78901234567890123456'),
(8, 3, 1, '89012345678901234567')
ON CONFLICT (empleado_id) DO NOTHING;

