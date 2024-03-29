<!DOCTYPE html>
<?php
$page = $_GET['page'] ?? '1'; // php >= 7.0
// in PHP < 7.0 (the old way)
//$id = isset($_GET['id']) ? $_GET['id'] : '1';
?>
<html lang="zxx" class="no-js">
<head>
  <!-- Mobile Specific Meta -->
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- Favicon-->
  <link rel="shortcut icon" href="../../~wbagais/waiting_room/img/fav.png">
  <!-- Author Meta -->
  <meta name="author" content="Wejdan">
  <!-- Meta Description -->
  <meta name="description" content="This website is for hospital waiting room">
  <!-- Meta Keyword -->
  <meta name="keywords" content="">
  <!-- meta character set -->
  <meta charset="UTF-8">
  <!-- Site Title -->
  <title>Waiting Room</title>

  <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,400,300,500,600,700" rel="stylesheet">
    <!--
    CSS
    ============================================= -->
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/linearicons.css">
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/font-awesome.min.css">
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/bootstrap.css">
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/magnific-popup.css">
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/jquery-ui.css">
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/nice-select.css">
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/animate.min.css">
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/owl.carousel.css">
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/jquery-ui.css">
    <link rel="stylesheet" href="../../~wbagais/waiting_room/css/main.css">
  </head>
  <body>
    <header id="header">
      <div class="container main-menu">
        <div class="row align-items-center justify-content-between d-flex">
          <div id="logo">
            <a href="../../~wbagais/waiting_room/index"><img src="../../~wbagais/waiting_room/img/logo.png" alt="" title="" /></a>
          </div>
          <nav id="nav-menu-container">
            <ul class="nav-menu">
              <li><a href="../../~wbagais/waiting_room/index.php">Home</a></li>
              <li><a href="../../~wbagais/waiting_room/physician.php">Physician</a></li>
              <li><a href="../../~wbagais/waiting_room/check_in.php">check In</a></li>
            </ul>
          </nav><!-- #nav-menu-container -->
        </div>
      </div>
    </header><!-- #header -->


    <!-- start banner Area -->
    <section class="banner-area relative about-banner" id="home">
      <div class="overlay overlay-bg"></div>
      <div class="container">
        <div class="row d-flex align-items-center justify-content-center">
          <div class="about-content col-lg-12">
            <h1 class="text-white">
              <?php echo strtoupper($page) ?>
            </h1>
            <p class="text-white link-nav"><a href="../../~wbagais/waiting_room/index.php">Home </a>  <span class="lnr lnr-arrow-right"></span>
              <a href=<?php echo "../../~wbagais/waiting_room/" . $page . ".php"?>> <?php echo $page ?></a></p>
          </div>
        </div>
      </div>
    </section>
    <!-- End banner Area -->
    <!-- Start team Area -->
      <section class="team-area section-gap">
          <div class="container">
              <div class="row d-flex justify-content-center">
                  <div class="menu-content pb-70 col-lg-7">
                      <div class="title text-center">
                          <h1 class="mb-10">

