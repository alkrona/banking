CREATE TABLE "transactions"(
"transaction_id" TEXT PRIMARY KEY,
"timestamp" NUMERIC,
"payee" TEXT,
"description" TEXT,
"raw_description" TEXT,
"amount" NUMERIC,
"balance" NUMERIC,
"receipt_number" TEXT,
"category" TEXT
);
CREATE TABLE "dimCategories"(
category TEXT PRIMARY KEY,
type TEXT
);