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

app.listen(PORT, () => {
  console.log(`Frontend running on port ${PORT}`);
});
