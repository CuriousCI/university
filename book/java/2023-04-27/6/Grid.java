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

	ArrayList<ArrayList<String>> descriptions;

	public Grid() {
		descriptions = new ArrayList<ArrayList<String>>();
	}

	public void add(int row, int column, String description) {
		while (descriptions.size() <= row)
			descriptions.add(new ArrayList<String>());

		while (descriptions.get(row).size() <= column)
			descriptions.get(row).add(null);

		descriptions.get(row).set(column, description);
	}

	public String getDescription(int row, int column) {
		return descriptions.get(row).get(column);
	}

	public ArrayList<Location> getDescribedLocations() {
		var locations = new ArrayList<Location>();

		for (var row = 0; row < descriptions.size(); row++)
			for (var col = 0; col < descriptions.get(row).size(); col++)
				if (descriptions.get(row).get(col) != null)
					locations.add(new Location(row, col));

		return locations;
	}

}
