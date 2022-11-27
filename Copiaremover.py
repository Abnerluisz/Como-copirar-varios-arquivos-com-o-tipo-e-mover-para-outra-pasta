function DELETE() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L11:BE14').activate();
  spreadsheet.getActiveRangeList().clear({contentsOnly: true, skipFilteredRows: true})
  .setBackground('BACKGROUND');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getCurrentCell().setValue('0');
  spreadsheet.getRange('H13').activate();
};

function MACRO2() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('1 ANO');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('2 ANOS');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('3 ANOS');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('4 ANOS');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('5 ANOS');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('6 ANOS');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('7 ANO');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('8 ANOS');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('9 ANOS');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12').activate();
  spreadsheet.getCurrentCell().setValue('10 ANOS');
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getActiveRangeList().setBackground('#202124');
  spreadsheet.getRange('G13').activate();
  spreadsheet.getRange('A36').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.setCurrentCell(spreadsheet.getRange('L13'));
  spreadsheet.getRange('L12:L13').insertCells(SpreadsheetApp.Dimension.COLUMNS);

  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.getActiveRangeList().setBackground('BACKGROUND');
  
};

function test() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('L12:L13').activate();
  spreadsheet.getActiveRangeList().setBackground('BACKGROUND');
};
