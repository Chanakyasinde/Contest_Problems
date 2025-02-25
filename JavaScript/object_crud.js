function createObjectFromArray(array, id) {
    const res={}
    array.forEach((val, ind) => {
        if (val!==null)
        res[ind]=val;
    })
    delete res[id];
    return res
}
