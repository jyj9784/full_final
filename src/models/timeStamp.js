const mongoose = require("mongoose");
const timeStampSchema = new mongoose.Schema({
  userEmail: {
    type: String,
    required: true,
  },
  time: {
    type: String,
    required: true,
  },
});

const timeStamp = mongoose.model("timeStamp", msgSchema);
module.exports = timeStamp;
