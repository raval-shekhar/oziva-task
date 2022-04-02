const redis = require('redis');
const publisher = redis.createClient();

publisher.connect()

/**
 * Returns a random number between min (inclusive) and max (inclusive)
 */
 function between(min, max) {  
    return Math.floor(Math.random() * (max - min + 1) + min)
}

/**
 * Publish data at interval of 1 second
 */
setInterval(async () => {
    const number = between(0, 999999)
    await publisher.publish('numbers', number);
    console.log(`SENT :: ${number}`);
}, 1000)
