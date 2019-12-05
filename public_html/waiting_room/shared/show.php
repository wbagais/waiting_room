<?php require_once("../../../private/initialize.php") ?>
<?php
$id = $_GET['id'] ?? '1'; // php >= 7.0
// in PHP < 7.0 (the old way)
//$id = isset($_GET['id']) ? $_GET['id'] : '1';
?>
<?php $page_title = 'Show Subject'; ?>
<?php include(SHARED_PATH . '/staff_header.php'); ?>

<div id = "content">
  <a class="back-link" href = "<?php echo url_for('/staff/subjects/index.php'); ?>">&laquo; Back to list</a>

  <div class = "Subject show">
    Subject ID: <?php echo h($id); ?>
  </div>
</div>

<?php include(SHARED_PATH . '/staff_footer.php'); ?>
