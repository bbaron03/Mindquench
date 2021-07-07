let past_ans = []
window.onload = function(){ // WHen the window loads, run the ajax function trying to get the past asnwers
    $.ajax({
        url: '/result',
        type: 'GET',
        success: function(response){//If it gets a json response from flask, sends the dict to the grid.
            dict_to_grid(response);
        },
        error: function(error){//Arbitrary error.
            console.log(error);
        }
    });
};

function dict_to_grid(arr){ //Will load the qresult document because of the flask render template running before this method
    let container = document.getElementById("answer_container");
    let counter = 0;
    if(arr.length > 0){
        let grid = document.createElement('table')
        grid.setAttribute('class', "col-lg-12")
        for(let i =0; i < arr.length;i++){
            let tr = document.createElement("tr");
            for(let j = 0; j < arr[i].length; j++){
                let cell = document.createElement("td");
                if(counter % 2 ==0){
                    cell.setAttribute('class', "col-lg-6 odd");
                }
                else{
                    cell.setAttribute('class', "col-lg-6 even");
                }
                cell.innerText = arr[i][j];
                tr.appendChild(cell);
            }
            counter++;
            grid.appendChild(tr);
        }
        container.appendChild(grid);
    }
}
