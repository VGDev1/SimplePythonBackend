const express = require('express');
const { quickSort } = require('./sort/quicksort');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.post('/api/sort', (req, res, next) => {
    const numbers = JSON.parse(req.body.numbers);
    const sorted = quickSort(numbers);
    res.json(sorted);
});

app.listen(3000, () => console.log('js app running on port 3000'));
