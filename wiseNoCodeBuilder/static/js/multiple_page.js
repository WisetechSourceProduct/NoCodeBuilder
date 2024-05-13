// Define a custom GrapesJS plugin
grapesjs.plugins.add('multiple-page-creator', (editor, opts = {}) => {
    // Define UI components for managing pages
    const addPageButton = document.createElement('button');
    addPageButton.innerHTML = 'Add Page';
    addPageButton.onclick = () => {
      // Logic to add a new page
      const newPage = editor.Pages.add({ name: 'New Page' });
      editor.set('selectedPage', newPage);
    };
  
    const removePageButton = document.createElement('button');
    removePageButton.innerHTML = 'Remove Page';
    removePageButton.onclick = () => {
      // Logic to remove the selected page
      const selectedPage = editor.Pages.getSelected();
      editor.Pages.remove(selectedPage);
    };
  
    // // Add UI components to the GrapesJS UI
    // editor.Panels.addButton('options', {
    //   id: 'add-page',
    //   className: 'fa fa-plus',
    //   command: 'add-page',
    //   attributes: { title: 'Add Page' },
    //   content: addPageButton,
    // });
  
    // editor.Panels.addButton('options', {
    //   id: 'remove-page',
    //   className: 'fa fa-minus',
    //   command: 'remove-page',
    //   attributes: { title: 'Remove Page' },
    //   content: removePageButton,
    // });
  
    // // Handle commands to add and remove pages
    // editor.Commands.add('add-page', {
    //   run: () => {
    //     // Logic to add a new page
    //     const newPage = editor.Pages.add({ name: 'New Page' });
    //     editor.set('selectedPage', newPage);
    //   },
    // });
  
    // editor.Commands.add('remove-page', {
    //   run: () => {
    //     // Logic to remove the selected page
    //     const selectedPage = editor.Pages.getSelected();
    //     editor.Pages.remove(selectedPage);
    //   },
    // });
  
    // Initialize the plugin
    return {};
  });
  