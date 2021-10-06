<?php
include 'phpqrcode/qrlib.php';
$text = "https://github.com/mr-vijaychauhan";

if (!empty($_POST)) {
    $text = $_POST['title'];
}

$path = 'images/';
$QRCode = $path . uniqid() . ".png";
// $ecc stores error correction capability('L')
$ecc = 'L';
$pixel_size = 8;
$frame_size = 2;

QRcode::png($text, $QRCode, $ecc, $pixel_size, $frame_size);
?>

<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>QR CODE Generator</title>
    <style>
        .bg-navbar,.bg-btn {
            background-color: #7952B3;
        }
    </style>
</head>

<body>
    <!-- Image and text -->
    <nav class="navbar navbar-light bg-navbar">
        <a class="navbar-brand" href="index.php">
           <!--  <img src="Untitled-1.png" width="30" height="30" class="d-inline-block align-top" alt=""> -->
            <span class="text-white">QRCode App</span>
        </a>
    </nav>
    <div class="container my-3">
        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <h5 class="card-header">Generate QR Code</h5>
                    <div class="card-body">
                        <form method="post">
                            <div class="form-group">
                                <input type="text" class="form-control" id="title" name="title" placeholder="Type Name or Website URL" required>
                            </div>
                            <input type="submit" class="btn bg-btn text-white" value="Generate">
                        </form>
                        <hr>
                        <div class="col-md-12">
                            <p>Generated of <span class="text-success"><?php echo $text; ?></span> QR Code</p>
                            <img src="<?php echo $QRCode; ?>"  class="border shadow" width="300" height="300">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>

</html>