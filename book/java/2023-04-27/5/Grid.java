import java.util.ArrayList;

public class Grid {
	/** Classe interna contenuta in Grid **/
	public static class Location {
		private int row;
		private int column;

		/**
		 * Create a location.
		 * 
		 * @param row    row of location
		 * @param column column of location
		 */
		public Location(int row, int column) {
			this.row = row;
			this.column = column;
		}

		/**
		 * Retrieve the row.
		 * 
		 * @return the row
		 */
		public int getRow() {
			return row;
		}

		/**
		 * Retrieve the column.
		 * 
		 * @return the column
		 */
		public int getColumn() {
			return column;
		}
	}

	String[][] descriptions;

	public Grid(int numRows, int numColumns) {
		descriptions = new String[numRows][numColumns];
	}

	public void add(int row, int column, String description) {
		descriptions[row][column] = description;
	}

	public String getDescription(int row, int column) {
		return descriptions[row][column];
	}

	public ArrayList<Location> getDescribedLocations() {
		var locations = new ArrayList<Location>();

		for (var row = 0; row < descriptions.length; row++)
			for (var col = 0; col < descriptions[row].length; col++)
				if (descriptions[row][col] != null)
					locations.add(new Location(row, col));

		return locations;
	}

}
