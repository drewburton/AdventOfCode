package day23;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
	private static HashSet<Elf> elves;

	public static void main(String... args) {
		File f = new File("day23/test.txt");
		// File f = new File("day23/input.txt");
		try (Scanner s = new Scanner(f)) {
			parseInput(s);
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
		}

		int i = 0;
		int direction = 0;
		proposeMoves(direciton);
		while (updatePositions()) {
			i++;
			if (i == 10) {
				System.out.println(countEmptyTiles());
				break;
			}
			direction = (direction + 1) % 4;
			proposeMoves(i);
		}
	}

	private static void parseInput(Scanner s) {
		int r = 0;
		while (s.hasNextLine()) {
			String line = s.nextLine();
			for (int c = 0; c < line.length(); c++) {
				if (line.charAt(c) == '#')
					elves.add(new Elf(r, c));
			}
			r++;
		}
	}

	private static void proposeMoves(int startingDirection) {
		HashMap<Elf, Elf> proposals = new HashMap<>();
		for (Elf e : elves) {
			if (!isElfInPosition(e.row - 1, e.col - 1) &&
					!isElfInPosition(e.row - 1, e.col) &&
					!isElfInPosition(e.row - 1, e.col + 1) &&
					!isElfInPosition(e.row, e.col - 1) &&
					!isElfInPosition(e.row, e.col + 1) &&
					!isElfInPosition(e.row + 1, e.col - 1) &&
					!isElfInPosition(e.row + 1, e.col) &&
					!isElfInPosition(e.row + 1, e.col + 1)) {
				// create proposal, create set of blocked proposals when two overlap

			}
		}

	}

	private static boolean updatePositions() {
		return false;
	}

	private static int countEmptyTiles() {
		return 0;
	}

	private static boolean isElfInPosition(int row, int col) {
		return elves.contains(new Elf(row, col));
	}
}

class Elf {
	int row, col;

	Elf(int row, int col) {
		this.row = row;
		this.col = col;
	}

	@Override
	public boolean equals(Object o) {
		Elf e = (Elf) o;
		if (e.row == row && e.col == col)
			return true;
		return false;
	}

	@Override
	public int hashCode() {
		return row * 7 + col * 31;
	}
}

class Proposal {

}