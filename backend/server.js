
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const Color = require('./Colormodel.js');

const app = express();
const port = 3001;

app.use(cors());
app.use(express.json());

mongoose.connect('mongodb+srv://Iirokopioi:Koodaan123@valot.mly8mhu.mongodb.net/?retryWrites=true&w=majority', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

Color.findOneAndUpdate({}, { red: false, yellow: false, green: false }, { upsert: true, new: true })
  .then(savedColor => {
    console.log('Default color saved:', savedColor);
  })
  .catch(err => {
    console.error(err);
  });

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get('/api/color/:id', async (req, res) => {
  try {
    const color = await Color.findOne({ boxId: req.params.id });
    if (!color) {
      return res.json({});
    }
    res.json(color);
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

app.put('/api/color/:id', async (req, res) => {
  try {
    console.log('PUT request received:', req.params.id, req.body);

    const { presetType, startTime, endTime, red, yellow, green } = req.body;

    const updatedColor = await Color.findOneAndUpdate(
      { boxId: req.params.id },
      { presetType, startTime, endTime, red, yellow, green },
      { new: true, upsert: true }
    );

    console.log('Updated color:', updatedColor);

    res.json(updatedColor);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal Server Error');
  }
});

app.use(express.static('build'));

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});