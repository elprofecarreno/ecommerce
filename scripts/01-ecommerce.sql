USE ecommerce;

/* JSON API CHILE https://apis.digital.gob.cl/dpa/regiones */
CREATE TABLE regiones_states (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  latitude  DECIMAL(9, 6),
  longitude DECIMAL(9, 6)
);

/* JSON API CHILE https://apis.digital.gob.cl/dpa/provincias */
CREATE TABLE provinces_townships (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  latitude DECIMAL(9, 6),
  longitude DECIMAL(9, 6),
  regiones_states_id INT,
  FOREIGN KEY (regiones_states_id) REFERENCES regiones_states(id)  
);

/* JSON API CHILE https://apis.digital.gob.cl/dpa/comunas */
CREATE TABLE communes_towns (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  latitude DECIMAL(9, 6),
  longitude DECIMAL(9, 6),
  provinces_townships_id INT,
  FOREIGN KEY (provinces_townships_id) REFERENCES provinces_townships(id) 
);

CREATE TABLE categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  description VARCHAR(150)
);

CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  description VARCHAR(150),
  sale_price DECIMAL(10, 2), 
  categories_id INT,
  FOREIGN KEY (categories_id) REFERENCES categories(id)
);

CREATE TABLE inventory (
  id INT AUTO_INCREMENT PRIMARY KEY,
  quantity INT,
  price INT,
  create_at TIMESTAMP,
  products_id INT,
  FOREIGN KEY (products_id) REFERENCES products(id)
);

CREATE TABLE addresses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  block VARCHAR(50),
  department VARCHAR(50),
  enumeration VARCHAR(10),
  latitude DECIMAL(9, 6),
  longitude DECIMAL(9, 6),
  zipcode INT,
  communes_towns_id INT,
  FOREIGN KEY (communes_towns_id) REFERENCES communes_towns(id)
);

CREATE TABLE offices (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  description VARCHAR(150),
  addresses_id INT,
  FOREIGN KEY (addresses_id) REFERENCES addresses(id)
);

CREATE TABLE genders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  description VARCHAR(150)
);

CREATE TABLE persons (
  id INT AUTO_INCREMENT PRIMARY KEY,
  national_identification VARCHAR(30) UNIQUE,
  names VARCHAR(50),
  lastname VARCHAR(120),
  second_lastname VARCHAR(120),
  genders_id INT,
  FOREIGN KEY (genders_id) REFERENCES genders(id) 
);

CREATE TABLE emails (
  id INT AUTO_INCREMENT PRIMARY KEY,
  mail VARCHAR(150),
  persons_id INT,
  FOREIGN KEY (persons_id) REFERENCES persons(id) 
);

CREATE TABLE phones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  phone VARCHAR(150),
  persons_id INT,
  FOREIGN KEY (persons_id) REFERENCES persons(id)   
);

CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  persons_id INT,
  communes_towns_id INT,
  FOREIGN KEY (persons_id) REFERENCES persons(id),
  FOREIGN KEY (communes_towns_id) REFERENCES communes_towns(id)
);

CREATE TABLE employees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  persons_id INT,
  communes_towns_id INT,
  offices_id INT,
  FOREIGN KEY (persons_id) REFERENCES persons(id),
  FOREIGN KEY (communes_towns_id) REFERENCES communes_towns(id),
  FOREIGN KEY (offices_id) REFERENCES offices(id)
);

CREATE TABLE documents (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  description VARCHAR(150)
);

CREATE TABLE sales (
  id INT AUTO_INCREMENT PRIMARY KEY,
  created_at TIMESTAMP,
  government_taxes DECIMAL(10, 2),
  state_taxes DECIMAL(10, 2),
  total DECIMAL(10, 2),
  documents_id INT,
  offices_id INT,
  FOREIGN KEY (documents_id) REFERENCES documents(id),
  FOREIGN KEY (offices_id) REFERENCES offices(id)
);

CREATE TABLE sales_details (
  id INT AUTO_INCREMENT PRIMARY KEY,
  price INT,
  quantity INT,
  total INT,
  sales_id INT,
  products_id INT,
  FOREIGN KEY (sales_id) REFERENCES sales(id),
  FOREIGN KEY (products_id) REFERENCES products(id)
);

CREATE TABLE payments_types (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  description VARCHAR(150)
);

CREATE TABLE payments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  amount DECIMAL(10, 2),
  payment_date DATE,
  sales_id INT,
  customers_id INT,
  payments_types_id INT,
  FOREIGN KEY (sales_id) REFERENCES sales(id),
  FOREIGN KEY (customers_id) REFERENCES customers(id),
  FOREIGN KEY (payments_types_id) REFERENCES payments_types(id)
);

CREATE TABLE shopping_session (
  id INT AUTO_INCREMENT PRIMARY KEY,
  customers_id INT,
  create_at TIMESTAMP,
  state BOOLEAN,
  FOREIGN KEY (customers_id) REFERENCES customers(id)
);

CREATE TABLE cart(
  price INT,
  quantity INT,
  products_id INT,
  shopping_session_id INT,
  FOREIGN KEY (products_id) REFERENCES products(id),
  FOREIGN KEY (shopping_session_id) REFERENCES shopping_session(id)
);