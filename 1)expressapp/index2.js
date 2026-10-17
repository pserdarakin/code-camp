import express from "express";

const app = express();
const port = 3000;

// TODO: forgot how to create middleware to turn body to json
app.use(express.json());

app.post("/tasks", (req, res) => {
  const title = req.body.title;
  const due_date = req.body.due_date;

  if (!title) {
    return res.status(400).json({ error: "title doesnt match" });
  }

  if (!due_date) {
    return res.status(400).json({ error: "due date doesnt match" });
  } else {
    res.status(201).json({ title, due_date });
  }
});

app.listen(port, () => {});

// POST /tasks
// takes a title and a due date (YYYY-MM-DD)
// returns 201 with the saved task
// returns 400 with a clear JSON error for a missing or empty title, a missing due date, an invalid date, or a body that is not JSON.
// One Jest and supertest test for each case.
// Plain JavaScript is fine.

// Step1. I need to import express setup express/app, listen on port, create middleware
