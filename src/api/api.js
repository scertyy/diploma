const url = '/api/';
const lc = localStorage;

export const api = {
    fetch : async (method, endpoint, body = null, token = false) => {
        let fetchArgs = {
            method: method,
            headers: {},
        };
        fetchArgs.headers['Content-Type'] = 'application/json'
        fetchArgs.headers['Accept'] = 'application/json'
        if (token) {
            lc.getItem('token_access') && (fetchArgs.headers['Authorization'] = `Bearer ${localStorage.getItem('token_access')}`)
        }
        body && (fetchArgs.body = JSON.stringify(body))
        return await fetch(url+endpoint, fetchArgs)
            .then(res => res.json())
    },

}