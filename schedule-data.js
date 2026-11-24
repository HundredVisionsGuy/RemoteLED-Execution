export default [
    // Monday's Schedule
    {
        day: "Mon",
        periods: [
            {
                period: 1,
                hall: "",
                startTime: (new Date()).setHours(8, 30, 0),
                endTime: (new Date().setHours(10, 2, 0))
            }, 
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(10, 2, 0),
                endTime: (new Date().setHours(10, 8, 0))
            },
            {
                period: 2,
                hall: "",
                startTime: (new Date()).setHours(10, 8, 0),
                endTime: (new Date().setHours(11, 40, 0))
            },
            // Students in south will move toward their Lunch period...
            // This should alternate each year
            {
                period: "Lunch",
                hall: "south",
                startTime: (new Date()).setHours(11, 40, 0),
                endTime: (new Date()).setHours(12, 14, 0)
            },
            {
                period: "Passing Time",
                hall: "south",
                startTime: (new Date()).setHours(12, 14, 0),
                endTime: (new Date().setHours(12, 20, 0))
            },
            {
                period: 3,
                hall: "south",
                startTime: (new Date()).setHours(12, 20, 0),
                endTime: (new Date().setHours(13, 52, 0))
            },
            {
                period: "Passing Time",
                hall: "north",
                startTime: (new Date()).setHours(11, 40, 0),
                endTime: (new Date().setHours(11, 46, 0))
            },
            {
                period: 3,
                hall: "north",
                startTime: (new Date()).setHours(11, 46, 0),
                endTime: (new Date().setHours(13, 18, 0))
            },
            {
                period: "Lunch",
                hall: "north",
                startTime: (new Date()).setHours(13, 18, 0),
                endTime: (new Date()).setHours(13, 52, 0)
            },
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(13, 52, 0),
                endTime: (new Date().setHours(13, 58, 0))
            },
            {
                period: 4,
                hall: "",
                startTime: (new Date()).setHours(13, 58, 0),
                endTime: (new Date()).setHours(15,30,0)
            },
        ]
    },
    // Tuesday's Schedule
    {
        day: "Tue",
        periods: [
            {
                period: 1,
                hall: "",
                startTime: (new Date()).setHours(8, 30, 0),
                endTime: (new Date().setHours(10, 2, 0))
            }, 
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(10, 2, 0),
                endTime: (new Date().setHours(10, 8, 0))
            },
            {
                period: 2,
                hall: "",
                startTime: (new Date()).setHours(10, 8, 0),
                endTime: (new Date().setHours(11, 40, 0))
            },
            // Students in south will move toward their Lunch period...
            // This should alternate each year
            {
                period: "Lunch",
                hall: "south",
                startTime: (new Date()).setHours(11, 40, 0),
                endTime: (new Date()).setHours(12, 14, 0)
            },
            {
                period: "Passing Time",
                hall: "south",
                startTime: (new Date()).setHours(12, 14, 0),
                endTime: (new Date().setHours(12, 20, 0))
            },
            {
                period: 3,
                hall: "south",
                startTime: (new Date()).setHours(12, 20, 0),
                endTime: (new Date().setHours(13, 52, 0))
            },
            {
                period: "Passing Time",
                hall: "north",
                startTime: (new Date()).setHours(11, 40, 0),
                endTime: (new Date().setHours(11, 46, 0))
            },
            {
                period: 3,
                hall: "north",
                startTime: (new Date()).setHours(11, 46, 0),
                endTime: (new Date().setHours(13, 18, 0))
            },
            {
                period: "Lunch",
                hall: "north",
                startTime: (new Date()).setHours(13, 18, 0),
                endTime: (new Date()).setHours(13, 52, 0)
            },
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(13, 52, 0),
                endTime: (new Date().setHours(13, 58, 0))
            },
            {
                period: 4,
                hall: "",
                startTime: (new Date()).setHours(13, 58, 0),
                endTime: (new Date()).setHours(15,30,0)
            },
        ]
    },
    // Wednesday's Schedule
    {
        day: "Wed",
        periods: [
            {
                period: 1,
                hall: "",
                startTime: (new Date()).setHours(9, 0, 0),
                endTime: (new Date().setHours(10, 15, 0))
            }, 
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(10, 15, 0),
                endTime: (new Date().setHours(10, 21, 0))
            },
            {
                period: 2,
                hall: "",
                startTime: (new Date()).setHours(10, 21, 0),
                endTime: (new Date().setHours(11, 36, 0))
            },
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(11, 36, 0),
                endTime: (new Date().setHours(11, 42, 0))
            },
            {
                period: "Advisory",
                hall: "",
                startTime: (new Date()).setHours(11, 42, 0),
                endTime: (new Date().setHours(12, 14, 0))
            },
            // Students in north will move toward their Lunch period...
            {
                period: "Lunch",
                hall: "south",
                startTime: (new Date()).setHours(12, 14, 0),
                endTime: (new Date()).setHours(12, 48, 0)
            },
            {
                period: "Passing Time",
                hall: "south",
                startTime: (new Date()).setHours(12, 48, 0),
                endTime: (new Date().setHours(12, 54, 0))
            },
            {
                period: 3,
                hall: "south",
                startTime: (new Date()).setHours(12, 54, 0),
                endTime: (new Date().setHours(14, 9, 0))
            },
            {
                period: "Passing Time",
                hall: "north",
                startTime: (new Date()).setHours(12, 14, 0),
                endTime: (new Date().setHours(12, 20, 0))
            },
            {
                period: 3,
                hall: "north",
                startTime: (new Date()).setHours(12, 20, 0),
                endTime: (new Date().setHours(13, 35, 0))
            },
            {
                period: "Lunch",
                hall: "north",
                startTime: (new Date()).setHours(13, 35, 0),
                endTime: (new Date()).setHours(14, 9, 0)
            },
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(14, 9, 0),
                endTime: (new Date().setHours(14, 15, 0))
            },
            {
                period: 4,
                hall: "",
                startTime: (new Date()).setHours(14, 15, 0),
                endTime: (new Date()).setHours(15, 30, 0)
            },
        ]
    },
    // Thursday's Schedule
    {
        day: "Thu",
        periods: [
            {
                period: 1,
                hall: "",
                startTime: (new Date()).setHours(8, 30, 0),
                endTime: (new Date().setHours(9, 49, 0))
            }, 
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(9, 49, 0),
                endTime: (new Date().setHours(9, 55, 0))
            },
            {
                period: 2,
                hall: "",
                startTime: (new Date()).setHours(9, 55, 0),
                endTime: (new Date().setHours(11, 14 , 0))
            },
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(11, 14, 0),
                endTime: (new Date().setHours(11, 20, 0))
            },
            // Access
            {
                period: "Access",
                hall: "",
                startTime: (new Date()).setHours(11, 20, 0),
                endTime: (new Date()).setHours(12, 6, 0)
            },
            // Students in the south will move toward their Lunch period...
            {
                period: "Lunch",
                hall: "south",
                startTime: (new Date()).setHours(12, 6, 0),
                endTime: (new Date()).setHours(12, 40, 0)
            },
            {
                period: "Passing Time",
                hall: "south",
                startTime: (new Date()).setHours(12, 40, 0),
                endTime: (new Date().setHours(12, 46, 0))
            },
            {
                period: 3,
                hall: "south",
                startTime: (new Date()).setHours(12, 46, 0),
                endTime: (new Date().setHours(14, 5, 0))
            },
            {
                period: "Passing Time",
                hall: "north",
                startTime: (new Date()).setHours(12, 6, 0),
                endTime: (new Date().setHours(12, 12, 0))
            },
            {
                period: 3,
                hall: "north",
                startTime: (new Date()).setHours(12, 12, 0),
                endTime: (new Date().setHours(13, 31, 0))
            },
            {
                period: "Lunch",
                hall: "north",
                startTime: (new Date()).setHours(13, 31, 0),
                endTime: (new Date()).setHours(14, 5, 0)
            },
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(14, 5, 0),
                endTime: (new Date().setHours(14, 11, 0))
            },
            {
                period: 4,
                hall: "",
                startTime: (new Date()).setHours(14, 11, 0),
                endTime: (new Date()).setHours(15, 30, 0)
            },
        ]
    },
    {
        day: "Fri",
        periods: [
            {
                period: 1,
                hall: "",
                startTime: (new Date()).setHours(8, 30, 0),
                endTime: (new Date().setHours(9, 49, 0))
            }, 
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(9, 49, 0),
                endTime: (new Date().setHours(9, 55, 0))
            },
            {
                period: 2,
                hall: "",
                startTime: (new Date()).setHours(9, 55, 0),
                endTime: (new Date().setHours(11, 14 , 0))
            },
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(11, 14, 0),
                endTime: (new Date().setHours(11, 20, 0))
            },
            // Access
            {
                period: "Access",
                hall: "",
                startTime: (new Date()).setHours(11, 20, 0),
                endTime: (new Date()).setHours(12, 6, 0)
            },
            // Students in the south will move toward their Lunch period...
            {
                period: "Lunch",
                hall: "south",
                startTime: (new Date()).setHours(12, 6, 0),
                endTime: (new Date()).setHours(12, 40, 0)
            },
            {
                period: "Passing Time",
                hall: "south",
                startTime: (new Date()).setHours(12, 40, 0),
                endTime: (new Date().setHours(12, 46, 0))
            },
            {
                period: 3,
                hall: "south",
                startTime: (new Date()).setHours(12, 46, 0),
                endTime: (new Date().setHours(14, 5, 0))
            },
            {
                period: "Passing Time",
                hall: "north",
                startTime: (new Date()).setHours(12, 6, 0),
                endTime: (new Date().setHours(12, 12, 0))
            },
            {
                period: 3,
                hall: "north",
                startTime: (new Date()).setHours(12, 12, 0),
                endTime: (new Date().setHours(13, 31, 0))
            },
            {
                period: "Lunch",
                hall: "north",
                startTime: (new Date()).setHours(13, 31, 0),
                endTime: (new Date()).setHours(14, 5, 0)
            },
            {
                period: "Passing Time",
                hall: "",
                startTime: (new Date()).setHours(14, 5, 0),
                endTime: (new Date().setHours(14, 11, 0))
            },
            {
                period: 4,
                hall: "",
                startTime: (new Date()).setHours(14, 11, 0),
                endTime: (new Date()).setHours(15, 30, 0)
            },
        ]
    }
]