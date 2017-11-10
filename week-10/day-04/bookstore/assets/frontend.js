'use strict'

let url = 'http://localhost:4000';
let bodyElement = document.querySelector('body');
let connectionObject = new XMLHttpRequest();

function talkToApi(method, resource, callback){
    connectionObject.open(method, url+resource, true);
    connectionObject.onload = function(){
        callback(connectionObject.response);      
    }
    connectionObject.send();
}

talkToApi("GET", "/list", createNameOfList);

function createNameOfList(response){
    let responseList = JSON.parse(response);
    console.log(responseList);   
    let tableData = "";
    let div = document.createElement('div');
    tableData = "<ul>";
    responseList.forEach(function(row) {
        tableData+="<li>"+ row.book_name +"</li>"
    });
    tableData+="</ul>";
    // div.innerHTML = responseText;
    div.innerHTML = tableData;
    bodyElement.appendChild(div);
    talkToApi("GET", "/table", createTableOfDatas);
}

function createTableOfDatas(responseData){
    let tableRows = JSON.parse(responseData);
    console.log(tableRows);
    let div = document.createElement('div');
    let tableInnerContent = `<table>
                    <thead>
                        <th>Book name</th>
                        <th>Author name</th>
                        <th>Category</th>
                        <th>Publisher name</th>
                        <th>Book price</th>
                    </thead>
                    <tbody>`;
    tableRows.forEach(function(row){
        tableInnerContent +=`<tr>
                        <td>`+ row.book_name +`</td>
                        <td>`+ row.aut_name +`</td>
                        <td>`+ row.cate_descrip +`</td>
                        <td>` + row.pub_name + `</td>
                        <td>`+ row.book_price +`</td>
                        </tr>`;
    });
    tableInnerContent+=`</tbody></table>`;
    div.innerHTML = tableInnerContent;
    bodyElement.appendChild(div);
}

// talkToApi("GET", "/all");