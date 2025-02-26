function sortObjectKeys(obj) {
    const sortedKeys = Object.keys(obj).sort();
    const sortedObj = {};
    
    for (let key of sortedKeys) {
        sortedObj[key] = obj[key];
    }
    
    return sortedObj;
}
