function processTransactions(users, requests)
{
// add transaction.
    let copiedUsers = JSON.parse(JSON.stringify(users));
    requests.forEach((request) => {
        let ind = -1;
        for (let i=0; i<copiedUsers.length; i++) {
            if (copiedUsers[i].id === request.user_id) {
                ind = i;
                break;
            }
        }
        if (request.withdraw !== undefined) {
            copiedUsers[ind].balance = (copiedUsers[ind].balance > request.withdraw) ? (copiedUsers[ind].balance - request.withdraw) : 0
            if (copiedUsers[ind].balance === 0) {
                copiedUsers[ind].status = "inactive"
            }
        }
        if (request.deposit !== undefined) {
            copiedUsers[ind].balance += request.deposit;
        }
        if (request.remove !== undefined) {
            copiedUsers[ind].balance = 0;
            copiedUsers[ind].status = "inactive";
        }
        if (request.activate !== undefined) {
            if (copiedUsers[ind].balance >= 100) copiedUsers[ind].status = "active";
        }
    })
    copiedUsers = copiedUsers.map((user) => {
        user.status = (user.balance >= 100)? "active" : "inactive";
        return user;
    })
    return copiedUsers;
}
