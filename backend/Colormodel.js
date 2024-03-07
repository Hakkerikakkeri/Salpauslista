const mongoose = require('mongoose');

const colorSchema = new mongoose.Schema({
  boxId: { type: Number, required: true },
  startTime: { type: String },
  endTime: { type: String },
  red: { type: Boolean, default: false },
  yellow: { type: Boolean, default: false },
  green: { type: Boolean, default: false },
  presetType: { type: String, enum: ['Normal', 'Blinking', 'Light off'], default: 'Normal' },
});

const Color = mongoose.model('Color', colorSchema);

module.exports = Color;