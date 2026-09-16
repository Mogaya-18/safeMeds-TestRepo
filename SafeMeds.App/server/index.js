const express = require("express");
const cors = require("cors");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("SafeMeds API is running");
});

// Import and mount route files here in future steps
// const vendorRoutes = require('./routes/vendors');
// app.use('/api/vendors', vendorRoutes);

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
