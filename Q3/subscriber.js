const redis = require('redis');

(async () => {
  const client = redis.createClient();
  const subscriber = client.duplicate();
  await subscriber.connect();
  /**
   * Listen to the data published on numbers channel
   */
  await subscriber.subscribe('numbers', (message) => {
    console.log(`Recieved :: ${message}`); // 'message'
  });
})();