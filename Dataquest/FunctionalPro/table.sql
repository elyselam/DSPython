CREATE TABLE wishlist (
    wishlist_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    name TEXT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id));