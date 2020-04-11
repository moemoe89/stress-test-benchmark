const http = require('http');
const port = '9102';
const app = new http.Server();

app.on('request', (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.write('NodeJS server');
  res.end('\n');
});

app.listen(port, () => {
  console.log(`Listening NodeJS server on ${port}`);
});