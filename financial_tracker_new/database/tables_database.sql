CREATE TABLE IF NOT EXISTS actual_balance (
	id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	actual_balance NUMERIC(10,2) CHECK(actual_balance >= 0.0)
);

CREATE TABLE IF NOT EXISTS transactions (
	id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name_expense VARCHAR(50) NOT NULL,
	price_expense NUMERIC(10,2) NOT NULL CHECK(price_expense > 0.0),
	type_expense VARCHAR(50) NOT NULL,
	date_expense TIMESTAMP NOT NULL
);


CREATE TABLE IF NOT EXISTS full_statistic (
	house_goods NUMERIC(10,2) CHECK(house_goods >= 0.0),
	food NUMERIC(10,2) CHECK(food >= 0.0),
	study NUMERIC(10,2) CHECK(study >= 0.0),
	entertainment NUMERIC(10,2) CHECK(entertainment >= 0.0),
	other NUMERIC(10,2) CHECK(other >= 0.0)
);
