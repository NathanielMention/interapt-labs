// This variable contains a list of words that is used to list the word distribution
var words = "Fourscore and seven years ago our fathers brought forth upon this continent a new nation " + 
            "conceived in liberty and dedicated to the proposition that all men are created equal " +
            "Now we are engaged in a great civil war testing whether that nation or any nation so conceived " +
			"and so dedicated can long endure We are met on a great battlefield of that war We have come " +
			"to dedicate a portion of it as a final resting place for those who died here that the nation " +
			"might live This we may in all propriety do But in a larger sense we cannot dedicate we cannot " +
			"consecrate we cannot hallow this ground The brave men living and dead who struggled here " + 
			"have hallowed it far above our poor power to add or detract The world will little note nor " +
			"long remember what we say here; while it can never forget what they did here " +	
			"It is rather for us the living we here be dedicated to the great task remaining before us " + 
			"that from these honored dead we take increased devotion to that cause for which they here gave " +
			"the last full measure of devotion that we here highly resolve that these dead shall not have died " +
			"in vain that this nation shall have a new birth of freedom and that government of the people " +
			"by the people for the people shall not perish from the earth" ;
/* This function creates the table: Not coded by students */
function showData( headings, keys, data ) {
	// Make a row of the table. Used for headings and data rows
	function makeRow( col1, col2 ) {
		return "<tr><td>" + col1 + "</td><td>" + col2 + "</td></tr>" ;
	}
	
	var tableString = "<table border='2'>"
	tableString     += "<caption>" + headings[ 0 ] + "</caption>" ;
	tableString     += makeRow( headings[ 1 ], headings[ 2 ] ) ;
	// Create rows: Col1 ==> Keys,  Col2 ==> Data
	for ( kIDX = 0; kIDX < keys.length; kIDX++ )
		tableString += makeRow( keys[ kIDX ], data[ keys[ kIDX ] ] ) ;
	
	tableString+= "</table>" ;
	document.getElementById("words").innerHTML = tableString ;
	
}