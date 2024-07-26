let custDetails = {
    custName: "Evan Kavanagh",
    birthDate: "2002-04-26",
    custGender: "Male",
    roomPref: ["Single Room", "Double Room", "Suite"],
    payMethod: "Debit Card",
    custAddress: {
        custStreet: "123 Placeholder Lane",
        custCity: "St. John's",
        custProv: "NL",
        custZip: "A1B 2C3"
    },
    calcAge: function() {
        const dateToday = new Date();
        const custBDay = new Date(this.birthDate);
        let custAge = dateToday.getFullYear() - custBDay.getFullYear();
        if (dateToday < new Date(dateToday.getFullYear(), custBDay.getMonth(), custBDay.getDate())) {
            custAge--;
        }
        return custAge;
    },
    phoneNum: "(123) 456-7890",
    checkinDate: "2024-02-14",
    checkoutDate: "2024-02-16",
    calcStay: function() {
        const checkIn = new Date(this.checkinDate);
        const checkOut = new Date(this.checkoutDate);
        const oneDay = 24 * 60 * 60 * 1000;
        const stayDays = Math.round((checkOut - checkIn) / oneDay);
        return stayDays;
    },
    custEmail: "placeholder123@gmail.com",
    custRequests: ["Extra Towels", "Room Service"],
    memberCheck: "Yes",

    custDesc: function() {
        let custAge = this.calcAge();
        let stayDays = this.calcStay();

        return `
        The customer's name is ${this.custName}.
        The customer is ${custAge} years old.
        The customer is ${this.custGender}.
        The customer's room preference(s) are ${this.roomPref.join(', ')}.
        The customer used ${this.payMethod} as a payment method.
        The customer's mailing address is ${this.custAddress.custStreet}, ${this.custAddress.custCity}, ${this.custAddress.custProv}, ${this.custAddress.custZip}.
        The customer's phone number is ${this.phoneNum}.
        The customer checked in on ${this.checkinDate}.
        The customer checked out on ${this.checkoutDate}.
        The customer stayed for ${stayDays} day(s).
        The customer's email is ${this.custEmail}.
        The customer's special request(s) are ${this.custRequests.join(', ')}.
        Is the customer apart of our loyalty membership program? ${this.memberCheck}.
        `;
    }
};

console.log(custDetails.custDesc());
document.write();