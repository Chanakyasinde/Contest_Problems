function processTransactions(users, transactions) {
    let updatedUsers = users.map(user => ({ ...user })); 

    for (let transaction of transactions) {
        let sender = updatedUsers.find(user => user.id === transaction.user_id1);
        let receiver = updatedUsers.find(user => user.id === transaction.user_id2);

        if (sender) {
            let senderBalance = sender.balance;
            if (senderBalance >= transaction.amount) {
                sender.balance -= transaction.amount; 
            } else {
                sender.balance -= transaction.amount; 
            }
        }

        if (receiver) {
            receiver.balance += transaction.amount; 
        }
    }

    return updatedUsers;
}
