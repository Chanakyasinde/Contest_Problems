function invertObject(obj) {
    const res={}
    for (const key in obj) {
        res[obj[key]] = key;
    }
    return res
}
