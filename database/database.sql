CREATE TABLE IF NOT EXISTS actual_balance (
    id INTEGER UNIQUE DEFAULT 1 CHECK (id = 1),
    actual_balance NUMERIC(10,2) NOT NULL CHECK (actual_balance >= 0)
);

INSERT INTO actual_balance (actual_balance)
VALUES (0)
ON CONFLICT (id) DO NOTHING;


CREATE TABLE IF NOT EXISTS type_expense (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO type_expense (name) VALUES 
    ('house goods'), 
    ('food'), 
    ('study'), 
    ('entertainment'), 
    ('other')
ON CONFLICT (name) DO NOTHING;


CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name_expense TEXT NOT NULL,
    price_expense NUMERIC(10,2) NOT NULL CHECK (price_expense > 0.0),
    type_expense_id INTEGER NOT NULL,
    date_expense TIMESTAMP NOT NULL,
    CONSTRAINT fk_type_expense 
        FOREIGN KEY (type_expense_id) 
        REFERENCES type_expense(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
