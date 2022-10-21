localStorage.clear();
    let table = document.getElementById("table");
    let carbs = 0, protein = 0, fats = 0, calories = 0;
    let count = table.rows.length

    for (var i=2; i<count-2; i++){
        console.log(table.rows[i].cells[1].innerHTML);
        carbs += parseFloat(table.rows[i].cells[1].innerHTML);
        carbs = Math.round(carbs);
        protein += parseFloat(table.rows[i].cells[2].innerHTML);
        protein = Math.round(protein);
        fats +=parseFloat(table.rows[i].cells[3].innerHTML); 
        fats = Math.round(fats);
        calories +=parseFloat(table.rows[i].cells[4].innerHTML);
        calories = Math.round(calories);
    };
    document.getElementById("totalCarbs").innerHTML = carbs;
    document.getElementById("totalProtein").innerHTML = protein;
    document.getElementById("totalFats").innerHTML = fats;
    document.getElementById("totalCalories").innerHTML = '<b>' + calories + '(Kcal)</b>';

    let calPer = (calories/2000)*100;
    document.getElementsByClassName("progress-bar")[0].setAttribute("style","width:"+calPer+"%");

    let total = carbs + protein + fats;
    let carbsP = Math.round((carbs/total)*100);
    let proteinP = Math.round((protein/total)*100);
    let fatsP = Math.round((fats/total)*100);




    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Carbs ' + carbsP + '%', 'Protein ' + proteinP + '%', 'Fats ' + fatsP + '%'],
        datasets: [{
            label: '# of Votes',
            data: [carbsP, proteinP , fatsP],
            backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
            ],
            borderWidth: 1
        }]
    }
});
