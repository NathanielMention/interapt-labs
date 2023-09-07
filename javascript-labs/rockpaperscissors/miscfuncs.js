// Display the computer pick using image returned by random generation
function showPicks( whoPickedId, imageFile ) {
	document.getElementById( whoPickedId ).innerHTML = 
	         "<p>" + whoPickedId + " picked :<img src='" + imageFile + "'/></p>"

}
// Show status of round and monies
function showStatusAndMonies( status, yourLoot, computerLoot ) {
	// Show status
	document.getElementById( 'status' ).innerHTML = status ;
	// Show monies
	document.getElementById( 'yourMoney' ).innerHTML = "You Have $" + yourLoot ;
	document.getElementById( 'computerMoney' ).innerHTML = "Computer has $" + computerLoot ;	
}