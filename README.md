# 📦 Populating the Database with Dummy Data

To facilitate **frontend development and testing**, a SQL script is provided to pre-populate your local database with a consistent set of mock data.
This script inserts **Users, Projects, Teams, and Workspaces**, ensuring you have a ready-to-use environment right after setup.

---

## ✅ Prerequisites

Before running the script, ensure that:

* PostgreSQL is installed and running (local machine or WSL).
* The PostgreSQL service is active.
* The `errgo` database has been created.
* All Prisma migrations have been applied:

```bash
npx prisma migrate dev
```

---

## ⚙️ Step 1: Configure the Script

1. Open the script file:

```
ERRGO_BE/pre-populate/pre-populate-env.sql
```

2. Locate the first line:

```sql
SET search_path TO 'schema_name';
```

3. Replace `'schema_name'` with your schema name.

   * For the default PostgreSQL schema, use:

```sql
SET search_path TO 'public';
```

4. Save and close the file.

---

## ▶️ Step 2: Run the Script

From the project root (`ERRGO_BE`), execute the script with:

```bash
psql -U postgres -d errgo -f pre-populate/pre-populate-env.sql
```

**Command breakdown:**

* `-U postgres` → PostgreSQL user (default: `postgres`)
* `-d errgo` → Database name
* `-f ...` → Path to the SQL file

👉 You will be prompted for the PostgreSQL password.

---

## 🔍 Step 3: Verify the Data

After running the script, verify that the mock data was inserted correctly.

### Option 1: Using Prisma Studio (recommended)

```bash
npx prisma studio
```

Navigate through the models (`Users`, `Projects`, `Teams`, `Workspaces`) to see the pre-populated data.

---

### Option 2: Using psql CLI

```bash
# Connect to the database
psql -U postgres -d errgo

# Run a query to check users
SELECT * FROM "users";
```

---

🎉 Your local environment is now populated with mock data and ready for **frontend development and testing**!
