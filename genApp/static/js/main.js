/**
 * Created by yansong on 10/26/2014.
 */
var rowNum = 0;
var formAtt = {};
function addRow(frm) {
    if(frm.property.value == '' || frm.datatype.value == ''){
        alert('property name and data type cannot be null!');
        return;
    }
    rowNum++;
    var cellName = '<td name="name[]">' + frm.property.value + '</td>';
    var cellType = '<td name="qty[]" >' + frm.datatype.value + '</td>';
    var cellBtn = '<td><input type="button" value="Remove" onclick="removeRow(' + rowNum + ');"></td>';
    var row = '<tr id="rowNum' + rowNum + '"> ' + cellName + cellType + cellBtn + '</tr>';
    $('#tb').append(row);
    formAtt[frm.property.value] = frm.datatype.value;
    frm.datatype.value = '';
    frm.property.value = '';
}

function removeRow(rnum) {
    var row_id = '#rowNum' + rnum;
    var rowCellName = $(row_id).children(':first').html();
    delete formAtt[rowCellName];
    $(row_id).remove();
}

function printForm() {
    console.log('print object contents ...');
    console.log(formAtt);
}