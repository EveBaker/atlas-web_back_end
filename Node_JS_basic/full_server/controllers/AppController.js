class AppControler {
    static getHomepage(res, req) {
        return res.status(200).send('Hello Holberton School!');
    }
}