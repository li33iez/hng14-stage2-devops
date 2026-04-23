const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();

// no hardcoded, port and URL are in the env
const API_URL = process.env.API_URL;
const PORT = process.env.PORT;

if (!API_URL) {
  throw new Error("API_URL is not defined in environment variables");
}

if (!PORT) {
  throw new Error("PORT is not defined in environment variables");
}

app.use(express.json());
app.use(express.static(path.join(__dirname, 'views')));

// Added for Docker HEALTHCHECK
app.get('/', (req, res) => {
  res.status(200).send('OK');
});

app.post('/submit', async (req, res) => {
  try {
    const response = await axios.post(`${API_URL}/jobs`);
    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/status/:id', async (req, res) => {
  try {
    const response = await axios.get(`${API_URL}/jobs/${req.params.id}`);
    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Added '0.0.0.0' so container is reachable
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Frontend running on port ${PORT}`);
}); // Added missing closing
