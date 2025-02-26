function createObjectFromArray(array, id) {
    let result = {};

    for (let index = 0; index < array.length; index++) {
        let value = array[index];
        if (value !== null && value % 2 === 0 && index !== id) {
            result[index] = value;
        }
    }

    return result;
}
