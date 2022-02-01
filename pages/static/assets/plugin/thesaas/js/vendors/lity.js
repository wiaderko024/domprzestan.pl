
/**
 * Load required plugin.
 */
window.Lity = require('pages/static/assets/plugin/thesaas/js/vendors/lity');

/**
 * Configure the plugin.
 */

+function($){
  page.registerVendor('Lity');

  page.initLity = function() {

    $(document).on('click', '[data-provide~="lightbox"]', Lity);

  }

}(jQuery);



